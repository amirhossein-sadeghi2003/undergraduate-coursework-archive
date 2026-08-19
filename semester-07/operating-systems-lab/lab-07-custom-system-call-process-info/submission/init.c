#include <errno.h>
#include <stdio.h>
#include <stdlib.h> 
#include <sys/syscall.h>
#include <unistd.h>
#include <linux/kernel.h>
#include <linux/sched.h>
struct process_info
{
	pid_t pid;
	char name[16];
	long state_str;
	unsigned long memory_usage;
};
const char* state_finder(long state)
{	
	if (state == 0){
		return "state of process is running.";
	}
	else if(state == 1){
		return "state of process is sleeping";
	}
	else{
		return "state of process is unknown.";
	}
}
int main(int argc, char* argv[])
{	while(1){	
		struct process_info my_process_information;
		pid_t pid;
		scanf("%d", &pid);
		syscall(548,pid, &my_process_information);
		printf("P_id your process is: %d\n", my_process_information.pid);
		printf("//////////////////////////////\n");
		printf("The state of your process is: %s\n", state_finder(my_process_information.state_str));
		printf("//////////////////////////////\n");
		printf("The usage of memory is: %lu\n", my_process_information.memory_usage);
		printf("//////////////////////////////\n");
		printf("your process name is: %s\n", my_process_information.name);
	}
}