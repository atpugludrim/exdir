#include<stdlib.h>
#include<stdio.h>
void f1(int a[], int i){
    printf("%d",a[i]);
}
void f2(int a[], int i){
    printf("%d", a[i-1]);
}
int main(int argc, char *argv[]){
    int N = atoi(argv[1]);
    int a[N];
    for(int i = 0;i<N;i++){
        a[i] = atoi(argv[2+i]);
    }
    f1(a,1);
    f2(a,2);
}
