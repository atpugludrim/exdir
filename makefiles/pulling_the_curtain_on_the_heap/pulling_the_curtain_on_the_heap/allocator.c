#define _GNU_SOURCE
#include<stdio.h>
#include<string.h>
#include<dlfcn.h>
#include<stdbool.h>
#include<stdint.h>
#include<stdlib.h>
#include "allocator.h"

typedef void * (*malloc_like_function) (size_t);
typedef void * (*free_like_function) (void *);

static malloc_like_function sysmalloc = NULL;
static free_like_function sysfree = NULL;

static bool init = false;
static FILE *fp = NULL;
static const char *logfilename = "allocs.log";

void initcheck(){
  if(!init){
    fp=fopen(logfilename, "w");
    init=true;
  }
}

void * malloc2(size_t size){
  initcheck();
  void *result = malloc(size);
  fprintf(fp, "M, %lu, %lu\n", (uintptr_t)result, size);
  return result;
}
void free2(void *p){
  initcheck();
  fprintf(fp, "F, %lu\n", (uintptr_t)p);
  free(p);
}
