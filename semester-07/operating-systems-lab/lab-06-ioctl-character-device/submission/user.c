#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <string.h>
#include <errno.h>



int main(void) {
    int volume_of_speaker = 100, new_volume;
    int fd = open("/dev/speakernode", O_RDWR);
    if (fd < 0) {
        perror("Can not open the device...");
        return errno;
    }

    
    
    if (ioctl(fd,  _IOW('s', 3, int), &volume_of_speaker) < 0) {
        perror("Some problem happened during setting volume_of_speaker");
        close(fd);
        return EXIT_FAILURE;
    }

    
    if (ioctl(fd, _IOR('s', 4, int), &new_volume) < 0) {
        perror("Some problem happened during getting volume_of_speaker");
        close(fd);
        return EXIT_FAILURE;
    }
    printf("Now volume_of_speaker is: %d\n", new_volume);


    
    char write_data[200] = "First testing audio.";
    if (write(fd, write_data, strlen(write_data)) < 0) {
        perror("Some problem happened during writing to the device...");
        return errno;
    }
    
    volume_of_speaker = 0;
    
    if (ioctl(fd,  _IOW('s', 3, int), &volume_of_speaker) < 0) {
        perror("Some problem happened during setting volume_of_speaker");
        close(fd);
        return EXIT_FAILURE;
    }

    
    if (ioctl(fd, _IOR('s', 4, int), &new_volume) < 0) {
        perror("Some problem happened during getting volume_of_speaker");
        close(fd);
        return EXIT_FAILURE;
    }
    printf("Now volume_of_speaker is: %d\n", new_volume);

    char write_data2[200] = "Second testing audio.";
    if (write(fd, write_data2, strlen(write_data2)) < 0) {
        perror("Some problem happened during writing to the device...");
        return errno;
    }

    volume_of_speaker = 50;
    
    if (ioctl(fd,  _IOW('s', 3, int), &volume_of_speaker) < 0) {
        perror("Some problem happened during setting volume_of_speaker");
        close(fd);
        return EXIT_FAILURE;
    }

    
    if (ioctl(fd, _IOR('s', 4, int), &new_volume) < 0) {
        perror("Some problem happened during getting volume_of_speaker");
        close(fd);
        return EXIT_FAILURE;
    }

    printf("Now volume_of_speaker is: %d\n", new_volume);

    char write_data3[200] = "Third testing audio.";
    if (write(fd, write_data3, strlen(write_data3)) < 0) {
        perror("Some problem happened during writing to the device...");
        return errno;
    }



    
    char read_data1[200];
    if (read(fd, read_data1, 200) < 0) {
        perror("Some problem happened during reading from the device...");
        return errno;
    }

    ioctl(fd, _IO('s', 1));
    

    char read_data2[200];
    if (read(fd, read_data2, 200) < 0) {
        perror("Some problem happened during reading from the device...");
        return errno;
    }

    ioctl(fd, _IO('s', 2));



    char read_data3[200];
    if (read(fd, read_data3, 200) < 0) {
        perror("Some problem happened during reading from the device...");
        return errno;
    }


    printf("First data read from device: %s\n", read_data1);
    printf("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n");
    printf("Second data read from device: %s\n", read_data2);
    printf("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n");
    printf("Third data read from device: %s\n", read_data3);
    printf("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n");

    close(fd);
    return 0;
}

