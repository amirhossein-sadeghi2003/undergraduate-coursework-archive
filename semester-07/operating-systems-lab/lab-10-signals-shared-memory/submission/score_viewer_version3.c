#include <signal.h>
#include <stdlib.h>
#include <fcntl.h>
#include "protocol.h"
#include <sys/mman.h>
#include <unistd.h>
#include <stdio.h>

void my_handler(int sig)
{
    int file_descriptor = shm_open(NAME, O_RDONLY, 0666);
    if (file_descriptor < 0)
    {
        perror("Some problem happened during calling shm_open()");
        return;
    }

    int size_shared_memory = NUM * sizeof(struct player);

    struct player *start_virtual_address = mmap(NULL, size_shared_memory, PROT_READ, MAP_SHARED, file_descriptor, 0);
    if (start_virtual_address == MAP_FAILED)
    {
        perror("Some problem happened during calling mmap()");
        return;
    }

    printf("New scores:\n");
    for (int i = 0; i < NUM; i++)
    {
        printf("%s, Score: %d\n", start_virtual_address[i].player_name, start_virtual_address[i].score);
    }

    munmap(start_virtual_address, size_shared_memory);
    close(file_descriptor);
}

int main()
{
    pid_t pid_reader = getpid();
    printf("PID of viewer is: %d\n", pid_reader);

    signal(SIGUSR1, my_handler);

    for (;;)
    {
        pause();
    }

    return 0;
}
