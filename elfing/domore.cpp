#include<iostream>
int domore(int x, int y){
    return x + y;
}
int main(int argc, char *argv[]){
    int i = 10, j = 20;
    std::cout << domore(i, j);
    return 0;
}
