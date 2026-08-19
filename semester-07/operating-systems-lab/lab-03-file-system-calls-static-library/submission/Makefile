all:compile

compile: main.o libmylib.a
	gcc main.o -L./ -lmylib -o my_app

main.o: main.c mylib.h
	gcc -c main.c
libmylib.a:mylib.o
	ar -r libmylib.a mylib.o
mylib.o:
	gcc -c mylib.c
clean:
	rm -f *.o *.a my_app
