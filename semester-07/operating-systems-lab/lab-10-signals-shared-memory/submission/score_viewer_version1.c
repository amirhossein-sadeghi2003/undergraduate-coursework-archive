#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include "protocol.h"

int main()
{
    int file_descriptor = shm_open(NAME, O_RDONLY, 0666);
    if (file_descriptor < 0)
    {
        perror("Some problem happend during calling shm_open()");
        return EXIT_FAILURE;
    }

    int size_of_shared_memory = NUM * sizeof(struct player);

    struct player *start_virtual_address = mmap(NULL, size_of_shared_memory, PROT_READ, MAP_SHARED, file_descriptor, 0);

    for (int i = 0; i < NUM; i++)
    {
        printf("%s, Score: %d\n", start_virtual_address[i].player_name, start_virtual_address[i].score);
    }

    if (shm_unlink(NAME) < 0)
    {
        perror("Some problem append during calling shm_unlink()");
        return EXIT_FAILURE;
    }

    printf("Removing shared memory.\n");

    munmap(start_virtual_address, size_of_shared_memory);
    close(file_descriptor);

    return EXIT_SUCCESS;
}
