#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include "protocol.h"
#include <sys/mman.h>
#include <unistd.h>
#include <string.h>
#include <time.h>

int main()
{
    int file_descriptor = shm_open(NAME, O_CREAT | O_RDWR, 0666);
    if (file_descriptor < 0)
    {
        perror("shm_open()");
        return EXIT_FAILURE;
    }

    int size_of_shared_memory = NUM * sizeof(struct player);
    ftruncate(file_descriptor, size_of_shared_memory);

    struct player *start_virtual_address = mmap(NULL, size_of_shared_memory, PROT_READ | PROT_WRITE, MAP_SHARED, file_descriptor, 0);
    if (start_virtual_address == MAP_FAILED)
    {
        perror("mmap()");
        return EXIT_FAILURE;
    }

    srand(time(NULL));
    for (int i = 0; i < NUM; i++)
    {
        snprintf(start_virtual_address[i].player_name, 50, "Amir_%d", i + 11);
        int my_random_score = (rand() % 100) + 1;
        start_virtual_address[i].score = my_random_score;
    }

    printf("Player data updated in shared memory.\n");

    munmap(start_virtual_address, size_of_shared_memory);
    close(file_descriptor);

    return EXIT_SUCCESS;
}
