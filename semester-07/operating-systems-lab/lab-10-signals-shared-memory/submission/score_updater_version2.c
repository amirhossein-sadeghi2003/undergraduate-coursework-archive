#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/mman.h>
#include <unistd.h>
#include "protocol.h"
#include <string.h>
#include <signal.h>

int main(int argc, char *argv[])
{

    pid_t pid_reader = atoi(argv[1]);
    if (pid_reader <= 0)
    {
        printf("PID is invalid.");
        return EXIT_FAILURE;
    }

    int file_descriptor = shm_open(NAME, O_CREAT | O_RDWR, 0666);
    if (file_descriptor < 0)
    {
        perror("Some problem happend during calling shm_open()");
        return EXIT_FAILURE;
    }

    int size_of_shared_memory = NUM * sizeof(struct player);
    ftruncate(file_descriptor, size_of_shared_memory);

    struct player *start_virtual_address = mmap(NULL, size_of_shared_memory, PROT_READ | PROT_WRITE, MAP_SHARED, file_descriptor, 0);
    if (start_virtual_address == MAP_FAILED)
    {
        perror("Some problem happend during calling mmap()");
        return EXIT_FAILURE;
    }

    srand(time(NULL));
    for (int i = 0; i < NUM; i++)
    {
        snprintf(start_virtual_address[i].player_name, 50, "Amir_%d", i + 11);
        int my_random_score = (rand() % 100) + 1;
        start_virtual_address[i].score = my_random_score;
    }

    while (1)
    {
        for (int i = 0; i < NUM; i++)
        {
            start_virtual_address[i].score = (rand() % 100) + 1;
        }

        printf("New scores are written in shared memory.\n");

        if (kill(pid_reader, SIGUSR1) == -1)
        {
            perror("kill()");
            return EXIT_FAILURE;
        }
        printf("Signal SIGUSR1 sent to score_viewer with PID: %d\n", pid_reader);

        sleep(3);
    }

    munmap(start_virtual_address, size_of_shared_memory);

    close(file_descriptor);

    return 0;
}
