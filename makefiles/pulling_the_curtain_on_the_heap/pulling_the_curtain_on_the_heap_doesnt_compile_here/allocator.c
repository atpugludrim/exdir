#define _GNU_SOURCE
#include<stdio.h>
#include<string.h>
#include<dlfcn.h>
#include<stdbool.h>
#include<stdint.h>

typedef void * (*malloc_like_function) (size_t);
typedef void * (*free_like_function) (void *);

static malloc_like_function sysmalloc = NULL;
static free_like_function sysfree = NULL;

static bool init = false;
static FILE *fp = NULL;
static const char *logfilename = "allocs.log";

void initcheck(){
  if (!init){
    sysmalloc = (malloc_like_function)dlsym(RTLD_NEXT, "malloc");
    sysfree = (free_like_function)dlsym(RTLD_NEXT, "free");
    fp = fopen(logfilename, "w");
    init = true;
  }
}

void * malloc(size_t size){
  initcheck();
  void *result = sysmalloc(size);
  fprintf(fp, "M, %lu, %lu\n", (uintptr_t)result, size);
  return result;
}
void free (void *p){
  initcheck();
  fprintf(fp, "F, %lu\n", (uintptr_t)p);
  sysfree(p);
}
