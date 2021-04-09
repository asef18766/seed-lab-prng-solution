all:
	gcc -c -fPIC prng.c -o prng.o
	gcc prng.o -shared -o libprng.so
clean:
	rm *.o *.so