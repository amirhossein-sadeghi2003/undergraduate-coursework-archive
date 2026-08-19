all: my_program

my_program: main.o prime_finder.o
	gcc -o my_program main.o prime_finder.o
main.o: main.c prime_finder.h
	gcc -c main.c
prime_finder.o:prime_finder.c prime_finder.h
	gcc -c prime_finder.c

install:my_program
	sudo cp my_program /usr/local/bin
uninstall:
	rm -f /usr/local/bin/my_program
clean:
	rm *.o my_program

