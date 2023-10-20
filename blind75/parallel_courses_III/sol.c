// https://leetcode.com/problems/parallel-courses-iii/
// note: I don't know why relationsColSize is provided (that too as a ptr!)
// since it'll always be 2.
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>
// C(n) = set of children of n
// t_n = time of node n
// T(n) = time until node n
// T(n) = max{T(m) | m \in C(n)} + t_n
// Memoize (DP).
// Top-Down or Bottom-Up (start from terminals and recurse down, or
// start from initials and go up).
// terminal: node that doesn't appear as fst (relation) for any relation \in relations
int *get_min_time_memoization;
int get_min_time(int n, int** parents, int* time, int curr){
  if(get_min_time_memoization[curr] == -1){
    int *cur_par = parents[curr];
    if (cur_par[0] == -1) // leaf - base case
      get_min_time_memoization[curr] = time[curr];
    int minTime = 0, ix, ret;
    for(ix=0; cur_par[ix]!=-1; ix++){
      ret = get_min_time(n, parents, time, cur_par[ix]);
      if (ret > minTime)
        minTime = ret;
    }
    get_min_time_memoization[curr] = minTime + time[curr];
  }
  return get_min_time_memoization[curr];
}
int minimumTime(int n, int** relations, int relationsSize, int* relationsColSize, int* time, int timeSize){
  bool *terminals = malloc(sizeof(bool)*n);
  int *termnls;
  int **parents, *tmppar;
  int minTime=-1;
  int parcnt;
  int ix, tcnt = 0, jx = 0, kx;
  get_min_time_memoization = malloc(sizeof(int)*n);
  memset(get_min_time_memoization, -1, sizeof(int)*n);
  parents = malloc(sizeof(parents)*n);
  memset(terminals, true, sizeof(bool)*n);
  for(ix = 0; ix < relationsSize; ix++){
    if(terminals[relations[ix][0]]){
      terminals[relations[ix][0]] = false;
      tcnt++;
    }
  }
  tcnt = n - tcnt;
  termnls = malloc(sizeof(int)*tcnt);
  for(ix = 0; ix < n; ix++){
    if(terminals[ix])
      termnls[jx++] = ix;
  }
  free(terminals);
  for(jx = 0; jx < n; jx++){
    parcnt = 0;
    for(ix = 0; ix < relationsSize; ix++){
      if(relations[ix][1] == jx)
        parcnt++;
    }
    tmppar = malloc(sizeof(int)*(parcnt+1));    // 1 extra space for -1 termination
    memset(tmppar, -1, sizeof(int)*(parcnt+1)); // -1 terminated
    kx = 0;
    for(ix = 0; ix < relationsSize; ix++){
      if(relations[ix][1] == jx){
        tmppar[kx++] = relations[ix][0];
      }
    }
    parents[jx] = tmppar;
  }
  // LOGIC GOES HERE
  for (ix = 0; ix < tcnt; ix++){
    kx = get_min_time(n, parents, time, termnls[ix]);
    if(kx > minTime)
      minTime = kx;
  }
  free(termnls);
  for(ix = 0; ix < n; ix++){
    free(parents[ix]);
  }
  free(parents);
  free(get_min_time_memoization);
  return minTime;
}
int main(int argc, char *argv[]){
  int n, m, a, b;
  scanf("%d", &n);
  scanf("%d", &m);
  int c = 2, ix;
  int **relations = malloc(sizeof(int*)*m);
  for(ix = 0; ix < m; ix++){
    relations[ix] = malloc(sizeof(int)*2);
    scanf("%d", &a);
    scanf("%d", &b);
    relations[ix][0] = a - 1; // 1-indexed
    relations[ix][1] = b - 1;
  }
  int *times = malloc(sizeof(int)*n);
  int time;
  for(ix = 0; ix < n; ix++){
    scanf("%d", &a);
    times[ix] = a;
  }
  time = minimumTime(n,relations,m,&c,times,n);
  free(times);
  for(ix = 0; ix < m; ix++){
    free(relations[ix]);
  }
  free(relations);
  printf("%d\n", time);
  return 0;
}
