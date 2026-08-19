#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>
#include <time.h>

#define NUM_THREADS 4

int *arr1, *arr2;
int total = 0;
sem_t mutex;

typedef struct {
    int id;
    int size;
    int start;
    int end;
} thread_info;

void* calc_dot_product(void* arg) {
    thread_info* info = (thread_info*)arg;
    int thread_id = info->id;
    int start_idx = info->start;
    int end_idx = info->end;
    
    int intermediate_result = 0;
    int i = start_idx;

    while (i < end_idx) {
        intermediate_result += arr1[i] * arr2[i];
        i++;
    }

    sem_wait(&mutex);
    total += intermediate_result;
    sem_post(&mutex);

    pthread_exit(NULL);
}

int main() {
    int size;

    printf("Enter the size of the arrays: ");
    scanf("%d", &size);

    arr1 = (int*)malloc(size * sizeof(int));
    arr2 = (int*)malloc(size * sizeof(int));

    printf("Enter values for the first array:\n");
    int i = 0;
    while (i < size) {
        scanf("%d", &arr1[i]);
        i++;
    }

    printf("Enter values for the second array:\n");
    i = 0;
    while (i < size) {
        scanf("%d", &arr2[i]);
        i++;
    }

    pthread_t thread_ids[NUM_THREADS];
    thread_info thread_params[NUM_THREADS];
    sem_init(&mutex, 0, 1);

    int chunk_size = size / NUM_THREADS;
    i = 0;

    while (i < NUM_THREADS) {
        thread_params[i].id = i;
        thread_params[i].size = size;
        thread_params[i].start = i * chunk_size;
        thread_params[i].end = (i == NUM_THREADS - 1) ? size : (i + 1) * chunk_size;

        pthread_create(&thread_ids[i], NULL, calc_dot_product, &thread_params[i]);
        i++;
    }

    i = 0;
    while (i < NUM_THREADS) {
        pthread_join(thread_ids[i], NULL);
        i++;
    }

    printf("Final product: %d\n", total);

    free(arr1);
    free(arr2);
    sem_destroy(&mutex);

    return 0;
}
