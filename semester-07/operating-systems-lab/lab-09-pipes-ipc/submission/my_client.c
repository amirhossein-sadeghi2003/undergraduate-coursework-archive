
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/stat.h>

#define NAME_OF_PIPE "/tmp/temperature_pipe"

typedef struct
{
    pid_t pid;
    int temperature;
} TemperatureData;
int main()
{
    int file_descriptor_pipe;
    file_descriptor_pipe = open(NAME_OF_PIPE, O_RDWR);
    TemperatureData information;
    information.pid = getpid();

    srand(time(NULL));
    while (1)
    {
        information.temperature = rand() % 41;
        write(file_descriptor_pipe, &information, sizeof(information));
        printf("Process with PID %d sent Temperature %d\n", information.pid, information.temperature);
        sleep(1);
        int lowest_temperature;
        read(file_descriptor_pipe, &lowest_temperature, sizeof(lowest_temperature));
        printf("Process with PID %d got minimum temperature %d\n", information.pid, lowest_temperature);

        sleep(3);
    }
    return 0;
}