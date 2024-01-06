#include <stdio.h>
#define DATAMAX 300001
int parent_or_size[DATAMAX];

int init(int n) {
    int i;
    for (i = 0; i <= n; i++)
        parent_or_size[i] = -1;
}

int leader(int a) {
    int parent = parent_or_size[a];
    if (parent_or_size[a] < 0)
        return a;
    return parent_or_size[a] = leader(parent_or_size[a]);
}

int merge(int a, int b) {
    int x = leader(a), y = leader(b), tmp;
    if (x == y)
        return x;
    if (-parent_or_size[x] < -parent_or_size[y]) {
        tmp = x;
        x = y;
        y = tmp;
    }
    parent_or_size[x] += parent_or_size[y];
    parent_or_size[y] = x;
    return x;
}

int same(int a, int b) {
    return leader(a) == leader(b);
}

int size(int a) {
    return -parent_or_size[leader(a)];
}

int main() {
    int n, i, u, v, max_num = 0, tmp;
    int ones[DATAMAX], onesize = 0;
    tmp = scanf("%d", &n);
    init(n);
    for (i = 0; i < n - 1; i++) {
        tmp = scanf("%d %d", &u, &v);
        if (u == 1) {
            ones[onesize] = v-1;
            onesize++;
            continue;
        } else if (v == 1) {
            ones[onesize] = u-1;
            onesize++;
            continue;
        }
        merge(u - 1, v - 1);
    }
    for (i = 0; i < onesize; i++) {
        tmp = size(ones[i]);
        if (tmp > max_num)
            max_num = tmp;
    }
    printf("%d\n", n - max_num);
    return 0;
}