#include<math.h>
#include<time.h>
#include<stdlib.h>
#include "allocator.h"

const int NUM_ITERATIONS=500;
const int MAX_SIZE=500;
const int MIN_SIZE=50;


void leaky_function(){
  void *p1 = malloc2(MIN_SIZE + (rand() % (MAX_SIZE-MIN_SIZE)));
  void *p2 = malloc2(MIN_SIZE + (rand() % (MAX_SIZE-MIN_SIZE)));
  void *p3 = malloc2(MIN_SIZE + (rand() % (MAX_SIZE-MIN_SIZE)));
  free2(p3);
  //free2(p2);
  free2(p1);
}
int main(int argc, char **argv){
  srand(time(NULL));
  for (int i = 0; i < NUM_ITERATIONS; i++){
    leaky_function();
  }
  return EXIT_SUCCESS;
}
