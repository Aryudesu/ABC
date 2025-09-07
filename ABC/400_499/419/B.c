#include <stdio.h>

#define MAX 102

int getMinIndex(int data[], int m) {
    int i;
    for (i = 0; i < m; i++) {
        if (data[i] > 0) {
            return i;
        }
    }
    return -1;
}

int main() {
    int data[MAX];
    int i, j, n, x;
    int Q;
    for (i = 0; i < MAX; i++) {
        data[i] = 0;
    }
    scanf("%d", &Q);
    for (i = 0; i < Q; i++) {
        scanf("%d", &n);
        if (n == 1) {
            scanf("%d", &x);
            data[x]++;
        } else if (n == 2) {
            j = getMinIndex(data, MAX);
            data[j]--;
            printf("%d\n", j);
        }
    }
    return 0;
}
