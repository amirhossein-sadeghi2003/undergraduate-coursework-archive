#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>
#define CHILD_COUNT 5

void perform_task(int task_id)
{

    srand(time(NULL) + getpid());

    int duration_time = rand() % 5 + 1;
    sleep(duration_time);

    printf("Task %d has been done by child %d in %d seconds\n", task_id, getpid(), duration_time);
    exit(0);
}

int main()
{
    pid_t processes[CHILD_COUNT];
    int process_status;

    int counter = 0;
    while (counter < CHILD_COUNT)
    {
        processes[counter] = fork();
        if (processes[counter] < 0)
        {
            perror("Some problem happend during calling fork().");
            exit(EXIT_FAILURE);
        }
        else if (processes[counter] == 0)
        {
            perform_task(counter + 1);
        }
        counter++;
    }

    counter = 0;
    while (counter < CHILD_COUNT)
    {
        pid_t finished_process = waitpid(processes[counter], &process_status, WNOHANG | WUNTRACED);

        if (finished_process > 0)
        {
            if (WIFEXITED(process_status))
            {
                printf("Process %d completed with exit code %d\n", finished_process, WEXITSTATUS(process_status));
            }
            else if (WIFSTOPPED(process_status))
            {
                printf("Process %d was stopped by signal %d\n", finished_process, WSTOPSIG(process_status));
            }
        }
        else if (finished_process == 0)
        {

            printf("Process %d is still running...\n", processes[counter]);
            sleep(1);
        }
        else
        {
            perror("Error during waitpid");
        }

        counter++;
    }
    return 0;
}
