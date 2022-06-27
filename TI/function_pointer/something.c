#include<stdio.h>
#include "something.h"
static int plusTwo(int a){
    printf("Returning %d from plusTwo\n", a+2);
    return a+2;
}
int sumPlusTwo(int a, int (*f2)(const void*, const void*), const void *b, const void *c){
    int retvar = plusTwo(a)+plusTwo(f2(b, c));
    printf("Returning %d from sumPlusTwo\n",retvar);
    return retvar;
}
