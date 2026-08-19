#ifndef MYLIB_H
#define MYLIB_H
#include <sys/types.h>


struct mystruct {
    uid_t owner;
    time_t lastModified;
    off_t fileSize;
};


void createFileWithPermission(const char* path, int permission);

int checkFile(const char* path, int permission);

struct mystruct showFileInfo(const char* path);


void createFileList(const char* dirPath, const char* prefix,const char* ext, int from, int to);
#endif
