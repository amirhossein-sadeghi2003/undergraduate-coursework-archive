#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>
#include <string.h>
#include <stdio.h>
#include <fcntl.h>
#include <time.h>
#include "mylib.h"
void createFileWithPermission(const char* path, int permission){
	int my_fd = open(path, O_CREAT | O_WRONLY, permission);
	chmod(path, permission);
         close(my_fd);
	 
}

int checkFile(const char *path, int permission) {
	int read_access = access(path, R_OK)+ 1;
	int write_access = access(path, W_OK) + 1;
	int exe_access = access(path, X_OK) + 1;
        int input_read_access;
	int input_write_access;
	int input_exe_access;
	int flag = 1 ;	
	if(permission == 7){
		input_read_access = 1;
		input_write_access = 1;
		input_exe_access = 1;

	}

	else if(permission == 6){
		input_read_access = 1;
                input_write_access = 1;
                input_exe_access = 0;
	
	}

	else if(permission == 5){
                input_read_access = 1;
                input_write_access = 0;
                input_exe_access = 1;

        }

	else if(permission == 4){
                input_read_access = 1;
                input_write_access = 0;
                input_exe_access = 0;

        }
        else if(permission == 3){
                input_read_access = 0;
                input_write_access = 1;
                input_exe_access = 1;

        }

	else if(permission == 2){
                input_read_access = 0;
                input_write_access = 1;
                input_exe_access = 0;
        }

	else if(permission == 1){
                input_read_access = 0;
                input_write_access = 0;
                input_exe_access = 1;


        }
	else if(permission == 0){
                input_read_access = 0;
                input_write_access = 0;
                input_exe_access = 0;
        }
	if(read_access == 0 && input_read_access == 1){
		printf("You can not read the file.\n");
		flag = 0;
	}
	
	if(write_access == 0 && input_write_access == 1){
                printf("You can not write into the file.\n");
		flag = 0;
        }

	if(exe_access == 0 && input_exe_access == 1){
                printf("You can not execute the file.\n");
		flag = 0;
        }
	if(flag == 1){
		printf("You have the permission");
	}



}



struct mystruct showFileInfo(const char *path) {
    struct stat file_info;
 

    struct mystruct fileInformation;
    fileInformation.owner = file_info.st_uid;
    fileInformation.lastModified = file_info.st_mtime;
    fileInformation.fileSize = file_info.st_size;

    
    printf("The Owner of file is : %d\n", fileInformation.owner);
    printf("Last modified: %s", ctime(&fileInformation.lastModified));
    printf("File size is: %ld bytes\n", fileInformation.fileSize);

    return fileInformation;
}





void createFileList(const char *dirPath, const char *prefix, const char *ext, int from, int to) {
    char path_of_file[1023];

    for (int counter = from; counter <= to; counter++){
        sprintf(path_of_file, "%s/%s_%d.%s", dirPath, prefix, counter, ext);
        int file_descriptor = open(path_of_file, O_CREAT | O_WRONLY, 0755);
        close(file_descriptor);
        printf("%s\n", path_of_file);
    }
}


