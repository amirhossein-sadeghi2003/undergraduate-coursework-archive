#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>
#include <sys/time.h>
int main()
{
    while (1)
    {
        struct timeval time_start;

        gettimeofday(&time_start, NULL);
        srand(time(NULL));
        struct timeval time_stop;
        pid_t pid_child = fork();
        if (pid_child < 0)
        {
            printf("Some problem happend during calling Fork().");
        }
        int my_random_number = (rand() % 5) + 1;
        if (pid_child == 0)
        {
            char inp[30];

            snprintf(inp, sizeof(inp), "%d", my_random_number);

            char *args[] = {"./app", inp, NULL};
            execv("./app", args);
        }
        int status_of_child;

        wait(&status_of_child);

        gettimeofday(&time_stop, NULL);

        long exact_time = (time_stop.tv_sec - time_start.tv_sec) * 1000 + (time_stop.tv_usec - time_start.tv_usec) / 1000;
        printf("%d        %d        %ld\n", pid_child, my_random_number, exact_time);
        printf("----------------------------\n");
    }
    return 0;
}
