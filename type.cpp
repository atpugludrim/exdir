#include<iostream>
#include<string>
#include<cstdlib>
#include<cstring>
#include<typeinfo>
using namespace std;
int main(int argc, char *argv[]){
  string s="";
  char s1[]="";
  char *s2 = (char *)malloc(sizeof(char));
  strcpy(s2,"");
  // these will be mangled name for gcc
  // ref: https://en.cppreference.com/w/cpp/types/type_info/name
  cout << typeid(s).name() << endl;
  cout << typeid(s1).name() << endl;
  cout << typeid(s2).name() << endl;
  cout << typeid("").name() << endl;
  cout << typeid(""s).name() << endl;
  cout << atoi('0'+"") << endl;
  // cout << stoi('0'+"") << endl;  <-- this fails converts to char[] literal
  cout << stoi('0'+""s) << endl; // <-- use string literal https://en.cppreference.com/w/cpp/string/basic_string
  cout << stoi(string(1, '0'));
  free(s2);
  return EXIT_SUCCESS;
  // further, in GDB use `(gdb) ptype <var>` or `(gdb) ptype <expression>`
  // or `(gdb) whatis <var or expr>
  // cannot check type of string literal using gdb
  // found this https://stackoverflow.com/questions/7429462/creating-c-string-in-gdb
}
