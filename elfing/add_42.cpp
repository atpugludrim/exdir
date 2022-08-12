#include<iostream>
int add_42(int);
int main(int argc, char *argv[]){
    int x = 10;
    std::cout << add_42(x);
    return 0;
}
int add_42(int n){
    return n + 42;
}
