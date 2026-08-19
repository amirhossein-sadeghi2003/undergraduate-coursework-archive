#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
void my_handler(int signum, siginfo_t *info)
{
    void *fault_addr = info->si_addr;
    printf("SIGSEGV is recived!\n");
    printf("You tried to access: %p\n", fault_addr);
    exit(1);
}

int main()
{
    struct sigaction info_sig;
    info_sig.sa_sigaction = my_handler;
    info_sig.sa_flags = 0;
    sigemptyset(&info_sig.sa_mask);

    if (sigaction(SIGSEGV, &info_sig, NULL) == -1)
    {
        perror("signal error...");
        return 1;
    }

    int *my_pointer = NULL;
    *my_pointer = 103;

    return 0;
}
