#include<stdio.h>
#include "external.h"
int main(int argc, char *argv[]){
  MyStruct *p = NULL;
  int a;
  MyStruct_create(&p);
  MyStruct_seta(5, p);
  MyStruct_geta(&a, p);
  printf("%d\n",a);
  return 0;
}
