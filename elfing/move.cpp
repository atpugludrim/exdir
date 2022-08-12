#include<iostream>
using namespace std;
int main(int argc, char *argv[]){
    int res;
    __asm__("movl $20, %%eax;"
            "movl $10, %%ebx;"
            "subl %%ebx, %%eax ":"=a"(res));
    cout<<res;
    return 0;
}
