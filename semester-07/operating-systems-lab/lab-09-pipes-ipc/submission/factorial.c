#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#define TOTAL_CHILDREN 5
int main()
{
    int number;
    printf("Enter a number between 0 and 21....\n");
    scanf("%d", &number);
    if (number < 1)
    {
        printf("Nmuber should be greater than 0.");
    }
    else if (number > 20)
    {
        printf("Number should be less than 21.");
    }
    int segment_size = number / TOTAL_CHILDREN;
    int pipe_fd[2];
    pid_t child_ids[TOTAL_CHILDREN];
    long long final_result = 1;
    pipe(pipe_fd);
    for (int i = 0; i < TOTAL_CHILDREN; i++)
    {
        child_ids[i] = fork();
        if (child_ids[i] == 0)
        {
            close(pipe_fd[0]);
            int begin = i * segment_size + 1;
            int end = (i == TOTAL_CHILDREN - 1) ? number : (i + 1) * segment_size;

            long long partial_factorial = 1;
            for (int j = begin; j <= end; j++)
            {
                partial_factorial *= j;
            }
            printf("Child %d computed the result: %lld\n", i + 1, partial_factorial);
            write(pipe_fd[1], &partial_factorial, sizeof(partial_factorial));
            close(pipe_fd[1]);
            exit(0);
        }
    }
    close(pipe_fd[1]);
    for (int i = 0; i < TOTAL_CHILDREN; i++)
    {
        long long partial_result;
        read(pipe_fd[0], &partial_result, sizeof(partial_result));
        final_result *= partial_result;
    }
    close(pipe_fd[0]);
    printf("The factorial of %d is %lld\n", number, final_result);
    return 0;
}