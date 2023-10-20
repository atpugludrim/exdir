// https://leetcode.com/problems/validate-binary-tree-nodes/?envType=daily-question&envId=2023-10-17
#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
int getSource(int n, int* leftChild, int* rightChild, int *src){
    // src owner is the function caller, must create space for it in the heap/stack before calling the function
    int *in_degrees, i, zct=0;
    in_degrees = malloc(sizeof(int)*n);
    if (in_degrees == NULL)
        return 1;
    memset(in_degrees, 0, sizeof(int)*n);
    for(i = 0; i < n; i++){
        if(leftChild[i] != -1)
          in_degrees[leftChild[i]]++;
        if(rightChild[i] != -1)
          in_degrees[rightChild[i]]++;
    }
    for(i = 0; i < n; i++){
        if(in_degrees[i] > 1){
            free(in_degrees);
            return 2;
        }
        else if(in_degrees[i] == 0){
            *src = i;
            zct++;
        }
    }
    free(in_degrees);
    if(zct != 1){
        return 3;
    }
    return 0;
}
int dfs(int src, int n, int* leftChild, int* rightChild, int* vis){
    int c;
    vis[src] = 1;
    // left child
    c = leftChild[src];
    if(c != -1){
        if(vis[c])
            return 1;
        if(dfs(c, n, leftChild, rightChild, vis))
            return 1;
    }
    // right child
    c = rightChild[src];
    if(c != -1){
        if(vis[c])
            return 1;
        if(dfs(c, n, leftChild, rightChild, vis))
            return 1;
    }
    return 0;
}
bool validateBinaryTreeNodes(int n, int* leftChild, int leftChildSize, int* rightChild, int rightChildSize){
    // find source: in-degree 0 (root), assert there's exactly one such node else return false
    // if there's a node with in-degree > 1, then also return false
    // do dfs from root, assert sure each node occurs only once in the dfs else return false (dfs ensures connected-ness)
    // assert(leftChildSize == rightChildSize)
    int r, src = -1, *vis;
    if (leftChildSize != rightChildSize && leftChildSize != n)
        return false;
    r = getSource(n, leftChild, rightChild, &src);
    if(r){
        return false;
    } 
    vis = malloc(sizeof(int)*n);
    memset(vis, 0, sizeof(int)*n);
    r = dfs(src, n, leftChild, rightChild, vis);
    if(r){
        free(vis);
        return false;
    }
    for(r = 0; r < n; r++){
        if(vis[r]!=1){
            free(vis);
            return false;
        }
    }
    free(vis);
    return true;
}
int main(int argc, char *argv[]){
    int n, i, tmp, *leftChild, *rightChild;
    bool r;
    scanf("%d", &n);
    leftChild = malloc(sizeof(int)*n);
    rightChild = malloc(sizeof(int)*n);
    for(i = 0; i < n; i++){
        scanf("%d", &tmp);
        leftChild[i] = tmp;
    }
    for(i = 0; i < n; i++){
        scanf("%d", &tmp);
        rightChild[i] = tmp;
    }
    r = validateBinaryTreeNodes(n, leftChild, n, rightChild, n);
    if(r){
        printf("true\n");
    }
    else{
        printf("false\n");
    }
    free(leftChild);
    free(rightChild);
    return 0;
}
