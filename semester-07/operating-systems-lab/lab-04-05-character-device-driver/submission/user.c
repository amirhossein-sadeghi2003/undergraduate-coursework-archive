#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>

#define device_path "/dev/module"
#define buff_len 200

int main(void){
	int fd = open (device_path, O_RDONLY);
	printf("fd: %d\n", fd);
    if(fd < 0){
        perror("open");
    }
    char buffer_for_write_data[buff_len] = "first example.";
    int result_write = write(fd, buffer_for_write_data, strlen(buffer_for_write_data));
    if ( result_write < 0) {
        printf("Error while writing.......");

    }

    char buffer_for_read_data[buff_len];
    if (read(fd, buffer_for_read_data, buff_len) < 0) {
        perror("can not read from device......");
        return errno;
    }
	close(fd);
}

















