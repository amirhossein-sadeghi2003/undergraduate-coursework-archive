#include <linux/uaccess.h>
#include <linux/kernel.h>

#include <linux/sched.h>
#include <linux/syscalls.h>


struct process_info{
	pid_t pid;
	char name[16];
	long state_str;
	unsigned long memory_usage;
};


SYSCALL_DEFINE2(sadeghi, pid_t, pid, struct process_info __user*, my_process_information)
{
	struct task_struct* task;
	struct process_info pcb_current_process;
	task = pid_task(find_vpid(pid), PIDTYPE_PID);
    if(!task)
        return -1;
	pcb_current_process.pid = task->pid;
	get_task_comm(pcb_current_process.name, task);
	pcb_current_process.state_str = task->__state;
    if(task->mm){
        pcb_current_process.memory_usage = task->mm->total_vm << PAGE_SHIFT;
    }
    else{
        pcb_current_process.memory_usage = 0;
    }
    if(copy_to_user(my_process_information, &pcb_current_process, sizeof(struct process_info)))
        return -EFAULT;
	return 0;
}