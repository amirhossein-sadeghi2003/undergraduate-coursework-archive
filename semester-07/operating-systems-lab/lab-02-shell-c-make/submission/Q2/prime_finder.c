#include "prime_finder.h"
#include <stdio.h>
int is_it_prime(int my_number){
	if(my_number <= 1){
		return 0;
	}
	for(int k = 2; k * k <= my_number; k++){
		if(my_number % k == 0){
			return 0;
		}
	}
	return 1;
}
