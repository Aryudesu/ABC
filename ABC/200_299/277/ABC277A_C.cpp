#include <stdio.h>


int calc() {
    int i;
    int n, x;
    int P[100];
    scanf("%d", &n);
    scanf("%d", &x);
    for (i = 0; i < n; i++){
        scanf("%d", &P[i]);
        if (P[i] == x)
            return i + 1;
    }
    return -1;
}


int main(){
    printf("%d", calc());
    return 0;
}