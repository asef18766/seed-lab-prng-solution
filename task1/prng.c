#include <stdlib.h>
#define KEYSIZE 16

void key_gen(char* key, int seed)
{
    int i;
    srand (seed);
    for (i = 0; i< KEYSIZE; i++){
        key[i] = rand()%256;
    }
}