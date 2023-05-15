#include<iostream>
#include<sstream>
#include<string>
using namespace std;
int main(int argc, char* argv[]){
    string s;
    stringstream ss(s);
    ss << "Hello " << 1 << " wow ";
    getline(ss, s);
    cout << s << endl;
    return 0;
}
