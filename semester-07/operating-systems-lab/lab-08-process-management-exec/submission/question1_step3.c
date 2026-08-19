#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>

#define MAX_PROCESSES 100

pid_t active_processes[MAX_PROCESSES];

void process_task(int id)
{
    srand(time(NULL) + getpid());
    int time_required = rand() % 5 + 1;
    // for (long long counter = 0; counter < 1000000000000000000 * time_required; counter++);
    while (1)
        ;
    printf("Task %d has been done by child %d after %d seconds\n", id, getpid(), time_required);
    exit(0);
}

int main()
{
    int state;

    int i = 0;
    while (i < MAX_PROCESSES)
    {
        active_processes[i] = fork();
        if (active_processes[i] < 0)
        {
            perror("Some problem happend during calling fork().");
            exit(EXIT_FAILURE);
        }
        else if (active_processes[i] == 0)
        {
            process_task(i + 1);
        }
        i++;
    }

    while (1)
    {
        sleep(5);
        for (int i = 0; i < MAX_PROCESSES; i++)
        {
            if (active_processes[i] > 0)
            {
                pid_t ended = wait(&state);
                if (ended > 0)
                {
                    /* if (WIFEXITED(state))
                     {
                         printf("Process %d finished with exit code %d\n", ended, WEXITSTATUS(state));
                     }
                     else if (WIFSTOPPED(state))
                     {
                         printf("Process %d was stopped by signal %d\n", ended, WSTOPSIG(state));
                     }*/
                    printf("Restarting task for process %d\n", ended);
                    active_processes[i] = fork();
                    if (active_processes[i] < 0)
                    {
                        perror("Error creating process");
                        exit(EXIT_FAILURE);
                    }
                    else if (active_processes[i] == 0)
                    {
                        process_task(i + 1);
                    }
                }
            }
        }
    }

    return 0;
}
