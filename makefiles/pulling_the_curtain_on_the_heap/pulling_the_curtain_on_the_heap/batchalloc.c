#include<math.h>
#include<time.h>
#include<stdlib.h>
#include "allocator.h"

const int NUM_ITERATIONS=500;
const int BATCH_SIZE=100;
const int MAX_SIZE=500;
const int MIN_SIZE=50;

int main(int argc, char **argv){
  srand(time(NULL));

  void *batch[BATCH_SIZE];
  for(int i=0; i < NUM_ITERATIONS; i++){
    for(int j=0; j < BATCH_SIZE; j++){
      batch[j] = malloc2(MIN_SIZE + (rand() % (MAX_SIZE-MIN_SIZE)));
    }
    for(int j=0; j < BATCH_SIZE; j++){
      free2(batch[BATCH_SIZE-1-j]);
    }
  }
  return EXIT_SUCCESS;
}
