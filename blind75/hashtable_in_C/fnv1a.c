#include<stdio.h>
#include<stdint.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>
struct LinkedList{
  int val, keylen;
  char *key;
  struct LinkedList* next;
};
typedef struct LinkedList LinkedList;
struct MyHashTable_str_to_int{
  int tsize;
  LinkedList **table;
};
typedef struct MyHashTable_str_to_int MyHashTable_str_to_int;
void freeLinkedList(LinkedList*);
void addToLinkedList(LinkedList**, int, char *);
bool LinkedListFind(LinkedList *, char *, int *);
bool insertHashTable(MyHashTable_str_to_int* obj, char *key, int val);
bool getHashTableKey(MyHashTable_str_to_int* obj, char *key, int *val);
MyHashTable_str_to_int* createHashTable(int tsize);
void freeHashTable(MyHashTable_str_to_int* obj);
uint64_t fnv1a(char *bytes, int num_bytes){
  uint64_t hash, prime;
  int i;
  hash = 0xcbf29ce484222325;
  prime = 0x100000001b3;
  for (i = 0; i < num_bytes; i++){
    hash = hash ^ bytes[i];
    hash = hash * prime;
  }
  return hash;
}
int main(int argc, char *argv[]){
  /* char *bytes, tmp;
  int n_bytes, ix, tsize;
  uint64_t hash;
  n_bytes = 80;
  tsize = 512;
  bytes = malloc(sizeof(*bytes) * n_bytes);
  for (ix = 0; ix < 10; ix++){
    scanf("%s", bytes);
    n_bytes = strlen(bytes);
    hash = fnv1a(bytes, n_bytes);
    printf("%s ", bytes);
    printf("%lu ", hash);
    printf("%lu\n", hash % tsize);
  }
  free(bytes);
  */
  MyHashTable_str_to_int* obj = createHashTable(512);
  char *hello;
  int val;
  bool ret;
  int idx;
  hello = malloc(sizeof(*hello)*(1+strlen("hello")));
  strcpy(hello, "hello");
  ret = insertHashTable(obj, hello, 1);
  printf("insert success code: %d\n", ret);
  idx = fnv1a(hello, strlen(hello)) % 512;
  printf("obj->table[%d]->key: %s\n", idx, obj->table[idx]->key);
  printf("obj->table[%d]->val: %d\n", idx, obj->table[idx]->val);
  ret = getHashTableKey(obj, hello, &val);
  printf("get success code: %d\n", ret);
  printf("%s %d\n", hello, val);
  // --------------------
  hello = malloc(sizeof(*hello)*(1+strlen("thankyou")));
  strcpy(hello, "thankyou");
  ret = insertHashTable(obj, hello, 2);
  printf("insert success code: %d\n", ret);
  idx = fnv1a(hello, strlen(hello)) % 512;
  printf("obj->table[%d]->key: %s\n", idx, obj->table[idx]->key);
  printf("obj->table[%d]->val: %d\n", idx, obj->table[idx]->val);
  ret = getHashTableKey(obj, hello, &val);
  printf("get success code: %d\n", ret);
  printf("%s %d\n", hello, val);
  // --------------------
  hello = malloc(sizeof(*hello)*(1+strlen("brand new")));
  strcpy(hello, "brand new");
  ret = insertHashTable(obj, hello, 3);
  printf("insert success code: %d\n", ret);
  idx = fnv1a(hello, strlen(hello)) % 512;
  printf("obj->table[%d]->key: %s\n", idx, obj->table[idx]->key);
  printf("obj->table[%d]->val: %d\n", idx, obj->table[idx]->val);
  ret = getHashTableKey(obj, hello, &val);
  printf("get success code: %d\n", ret);
  printf("%s %d\n", hello, val);
  // --------------------
  freeHashTable(obj);
  return 0;
}
MyHashTable_str_to_int* createHashTable(int tsize){
  int ix;
  MyHashTable_str_to_int *obj;
  obj = malloc(sizeof(*obj));
  obj->tsize = tsize;
  obj->table = malloc(sizeof(obj->table)*tsize);
  for(ix = 0; ix < tsize; ix++){
    obj->table[ix] = NULL;
  }
  return obj;
}
void freeHashTable(MyHashTable_str_to_int* obj){
  int ix;
  for(ix = 0; ix < obj->tsize; ix ++){
    freeLinkedList(obj->table[ix]);
  }
  free(obj->table);
  free(obj);
}
void freeLinkedList(LinkedList* head){
  if(head == NULL)
    return;
  freeLinkedList(head->next);
  free(head->key);
  free(head);
}
void addToLinkedList(LinkedList** head, int val, char *key){
  LinkedList *new_node = malloc(sizeof(*new_node)), *tmp;
  new_node->val = val;
  new_node->key = key;
  new_node->keylen = strlen(key);
  new_node->next = NULL;
  if(*head == NULL)
    *head = new_node;
  else{
    tmp = *head;
    while(tmp->next != NULL){
      tmp = tmp->next;
    }
    tmp->next = new_node;
  }
}
bool insertHashTable(MyHashTable_str_to_int* obj, char *key, int val){
  int l = strlen(key);
  uint64_t hash = fnv1a(key, l);
  int idx = hash % obj->tsize;
  int flag;
  LinkedList *hashlist;
  hashlist = obj->table[idx];
  flag = hashlist == NULL;
  if(!LinkedListFind(hashlist, key, &l)){
    addToLinkedList(&hashlist, val, key);
    if (flag){
      obj->table[idx] = hashlist;
    }
    return true;
  }
  return false;
}
bool LinkedListFind(LinkedList *head, char *key, int *val){
  if (head == NULL)
    return false;
  int keylen = strlen(key);
  while(head != NULL){
    if(head->keylen == keylen){
      if(!strcmp(key, head->key)){
        *val = head->val;
        return true;
      }
    }
    head = head->next;
  }
  return false;
}
bool getHashTableKey(MyHashTable_str_to_int* obj, char *key, int *val){
  int l = strlen(key);
  uint64_t hash = fnv1a(key, l);
  int idx = hash % obj->tsize;
  LinkedList *hashlist;
  hashlist = obj->table[idx];
  return LinkedListFind(hashlist, key, val);
}
