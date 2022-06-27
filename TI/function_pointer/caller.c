#include<stdio.h>
#include "something.h"
int times(const void *a, const void *b){
    int A = *((int*)a);
    int B = *((int*)b);
    printf("Returning %d from times\n",A*B);
    return A*B;
}
int main(int argc, char* argv[]){
    int a = 5;
    int b = 3;
    int c = 7;
    int retvar = sumPlusTwo(a,times,(void *)&b, (void *)&c);
    printf("Output = %d. Should be equal to (5+2)+(3x7+2) = 7+21+2 = 30\n",retvar);
    // printf("%d",func1(a)); // causes undefined reference
    return 0;
}
