#include<stdlib.h>
struct MyStruct{
  int a;
};
typedef struct MyStruct MyStruct;
int MyStruct_create(MyStruct **pp){
  MyStruct *p = (MyStruct *)malloc(sizeof(MyStruct));
  *pp = p;
  return 0;
}
int MyStruct_seta(int a, MyStruct *p){
  p->a = a;
  return 0;
}
int MyStruct_geta(int *a, MyStruct *p){
  *a = p->a;
  return 0;
}
