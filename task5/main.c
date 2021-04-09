#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define KEYSIZE 256/8
void main()
{
    int i;
    char key[KEYSIZE];
    FILE* random = fopen("/dev/urandom", "r");
    fread(key, sizeof(char)*KEYSIZE, 1, random);

    for (i = 0; i< KEYSIZE; i++){
        printf("%.2x", (unsigned char)key[i]);
    }
    printf("\n");
}