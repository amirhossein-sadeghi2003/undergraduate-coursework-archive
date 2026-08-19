#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <fcntl.h>
#include <sys/mman.h>
#include "protocol.h"
#include <unistd.h>
#include <string.h>
#include <signal.h>

int main(int argc, char *argv[])
{

    pid_t pid_reader = atoi(argv[1]);
    if (pid_reader <= 0)
    {
        printf("Input PID is invalid.");
        return EXIT_FAILURE;
    }

    int file_descriptor = shm_open(NAME, O_CREAT | O_RDWR, 0666);
    if (file_descriptor < 0)
    {
        perror("Some problem happend durig callig shm_open()");
        return EXIT_FAILURE;
    }

    int size_shared_memory = NUM * sizeof(struct player);
    ftruncate(file_descriptor, size_shared_memory);

    struct player *start_virtual_address = mmap(NULL, size_shared_memory, PROT_READ | PROT_WRITE, MAP_SHARED, file_descriptor, 0);
    if (start_virtual_address == MAP_FAILED)
    {
        perror("Some problem happend during calling mmap()");
        return EXIT_FAILURE;
    }

    while (1)
    {
        for (int child_id = 0; child_id < 5; child_id++)
        {
            pid_t pid = fork();

            if (pid < 0)
            {
                perror("Some problem happend during calling fork()");
                return EXIT_FAILURE;
            }

            if (pid == 0)
            {
                srand(time(NULL) + getpid());
                int id_first_person = child_id;
                for (int i = id_first_person; i < NUM; i += 5)
                {
                    snprintf(start_virtual_address[i].player_name, 50, "Amir_%d", i + 11);
                    int my_random_score = (rand() % 100) + 1;
                    start_virtual_address[i].score = my_random_score;
                }

                exit(0);
            }
        }

        int counter = 5;
        while (counter > 0)
        {
            wait(NULL);
            counter--;
        }

        if (kill(pid_reader, SIGUSR1) == -1)
        {
            perror("Some problem happend during sending SIGUSR1.");
            return EXIT_FAILURE;
        }
        printf("Signal SIGUSR1 is sent to process: %d\n", pid_reader);

        sleep(3);
    }

    munmap(start_virtual_address, size_shared_memory);
    close(file_descriptor);

    return 0;
}
