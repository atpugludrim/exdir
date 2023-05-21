#include<stdio.h>
#include<unistd.h>
#include<sys/syscall.h>

int returny_func(int *a, char b, short c, int d){
    return b+c;
}
int main(int argc, char* argv[]){
    long long mylong = 0xbabecafef00dface;
    int myint = 0xdeadf00d;
    char str[] = "mystr";
    int i = 1337;
    while(i){
        i--;
    }
    int ret = returny_func(&i, 0x42, 0x69, 0x31337);
    syscall(SYS_write, 1, "done:)\n", 7);
    return 32;
}
