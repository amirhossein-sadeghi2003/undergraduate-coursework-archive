#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <sys/mman.h>
#include <semaphore.h>
#include <fcntl.h>
#include <sys/types.h>
int *readCount, *source;
sem_t *readSem, *sourceSem;
void function_for_writing(int process_id) {
    for (;;) {
        srand(time(NULL));
        sem_wait(sourceSem);
        int my_random = (rand() % 10) + 1;
        *source += my_random;
        printf("process with id %d writes %d.Score is updated.\n", process_id, *source);
        int my_second_random_number = (rand() % 3) + 1;
        sleep(my_second_random_number);
        sem_post(sourceSem);
        int my_third_random_number = (rand() % 3) + 1;
        sleep(my_third_random_number);
    }
}
void function_for_reading(int process_id) {
    for (;;) {
        sem_wait(readSem);
        (*readCount)++;
        (*readCount == 1) ? sem_wait(sourceSem) : 0;
        sem_post(readSem);

        printf("Process with id %d read the value of variable source = %d.\n", process_id, *source);
        int my_random_number = (rand() % 3) + 1;
        sleep(my_random_number);

        sem_wait(readSem);
        (*readCount)--;
        (*readCount == 0) ? sem_post(sourceSem) : 0;
        sem_post(readSem);
        int my_second_random_number = (rand() % 3) + 1;
        sleep(my_second_random_number);
    }
}
int main() {
    int number_of_readers_process, number_of_writer_process;
    void *shm = mmap(NULL, 2 * sizeof(sem_t) + 2 * sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    readSem = (sem_t *)shm;
    sourceSem = (sem_t *)(shm + sizeof(sem_t));
    readCount = (int *)(shm + 2 * sizeof(sem_t));
    source = (int *)(shm + 2 * sizeof(sem_t) + sizeof(int));
    *readCount = 0;
    *source = 0;

    sem_init(readSem, 1, 1);
    sem_init(sourceSem, 1, 1);

    srand(time(NULL));

    printf("Enter the number of readers: ");
    scanf("%d", &number_of_readers_process);
    printf("Enter the number of writers: ");
    scanf("%d", &number_of_writer_process);

    pid_t pid_child_process;
    int i = 0;
    while (i < number_of_readers_process) {
        pid_child_process = fork();
        if (pid_child_process == 0) {
            int id_process = i + 100;
            function_for_reading(id_process);
        }
        i++;
    }

    i = 0;
    while (i < number_of_writer_process) {
        pid_child_process = fork();
        if (pid_child_process == 0) {
            int id_process = i + 100;
            function_for_writing(id_process);
        }
        i++;
    }

    
    while (1) {
        wait(NULL);
        
    }

    sem_destroy(readSem);
    sem_destroy(sourceSem);

    munmap(shm, 2 * sizeof(sem_t) + 2 * sizeof(int));

    return 0;
}
