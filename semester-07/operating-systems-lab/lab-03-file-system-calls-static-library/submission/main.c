#include <stdio.h>
#include <string.h>
#include<stdlib.h>
#include "mylib.h"

int main(int argc, char *argv[]) { 

    if (strcmp(argv[1], "-c") == 0 && argc == 4) {
            const char *path_of_file = argv[2];
            int permission = (int)strtol(argv[3], NULL, 8);  
            createFileWithPermission(path_of_file, permission);
            printf("The file is created at %s and the permission is %o\n", path_of_file, permission);
    } 
    else if (strcmp(argv[1], "-t") == 0 && argc == 4) {
     
        const char *path_of_file = argv[2];
        int permission = (int)strtol(argv[3], NULL, 8);
        checkFile(path_of_file, permission);
    }


    else if (strcmp(argv[1], "-s") == 0 && argc == 3) {
     
        const char *path_of_file = argv[2];
        showFileInfo(path_of_file);
    }


    else if (strcmp(argv[1], "-m") == 0 && argc == 7) {
  
        const char *dirPath = argv[2];
        const char *prefix = argv[3];
        const char *ext = argv[4];
        int start = atoi(argv[5]);
        int end = atoi(argv[6]);
        createFileList(dirPath, prefix, ext, start, end);
    }

    return 0;
}


	
