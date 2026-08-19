#include <stdio.h>
#include "prime_finder.h"
int main(int argc, char *argv[]){
	if(argc < 2){
		printf("invalid input");
		return 1;
	}
	for(int y = 1; y < argc; y++){
		int number = atoi(argv[y]);
		if(is_it_prime(number)){
			printf("%d is prime.\n", number);
		}
		else{
			printf("%d is not prime\n", number);
		}

	}
	return 0;
}
