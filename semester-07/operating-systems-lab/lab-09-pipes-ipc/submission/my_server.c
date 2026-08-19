#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <string.h>
#include <time.h>
#include <sys/types.h>
#define NAME_OF_PIPE "/tmp/temperature_pipe"

typedef struct
{
    pid_t pid;
    int temperature;
} TemperatureData;
int main()
{

    mkfifo(NAME_OF_PIPE, 0777);
    int file_descriptor_pipe;
    file_descriptor_pipe = open(NAME_OF_PIPE, O_RDWR);
    TemperatureData information;
    int lowest_temperature = 350;
    printf("server is ready.\n");
    int infinite_loop;
    for (infinite_loop = 0; infinite_loop > -1; infinite_loop++)
    {
        read(file_descriptor_pipe, &information, sizeof(TemperatureData));
        printf("Process with PID %d sent temperature %d\n", information.pid, information.temperature);

        lowest_temperature = (information.temperature < lowest_temperature) ? information.temperature : lowest_temperature;

        write(file_descriptor_pipe, &lowest_temperature, sizeof(lowest_temperature));
        printf("Minimum temperature sent to client: %d\n", lowest_temperature);
        sleep(1);
    }
    return 0;
}