// https://leetcode.com/problems/design-add-and-search-words-data-structure/
// next -> https://leetcode.com/problems/all-oone-data-structure/
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include<stdio.h>
struct WordDictionary{
  int size;
  char *p;
};
typedef struct WordDictionary WordDictionary;
WordDictionary* wordDictionaryCreate(){
  WordDictionary *dict;
  dict = malloc(sizeof(WordDictionary));
  dict->size = 0;
  return dict;
}
void wordDictionaryAddWord(WordDictionary** objptr, char *word){
  int l, s;
  l = strlen(word) + 1; // null character \0
  s = (*objptr)->size;
  (*objptr) = realloc((*objptr), sizeof(WordDictionary) + s + l + 1);
  (*objptr)->p = (char *)(&((*objptr)->p) + 1);
  (*objptr)->size += l;
  memcpy((*objptr)->p+s, word, l);
}
bool wordDictionarySearch(WordDictionary* obj, char *word){
  char *ptr = obj->p;
  int size = obj->size, ix, jx;
  int flag = 1;
  int matches_dot = 0;
  int l = strlen(word);
  jx = 0;
  if (size == 0){
    return false;
  }
  for(ix = 0; ix < size; ix++, jx++){
    if(ptr[ix] == '\0'){
      if(flag == 1 && jx == l)
        return true;
      flag = 1;
      jx = 0;
      ix++;
    }
    else if(word[jx] == '\0'){
      flag = 0;
    }
    matches_dot = !(ptr[ix] == word[jx] || word[jx] == '.');
    if(flag && matches_dot){
      flag = 0;
    }
  }
  return false;
}
void wordDictionaryFree(WordDictionary* obj){
  free(obj);
}
int main(int argc, char *argv[]){
  WordDictionary* dict = wordDictionaryCreate();
  bool result;
  wordDictionaryAddWord(&dict, "hello");
  wordDictionaryAddWord(&dict, "hi");
  wordDictionaryAddWord(&dict, "henlo");
  result = wordDictionarySearch(dict, "he..o");
  wordDictionaryFree(dict);
  printf("%d\n", result);
  return 0;
}
