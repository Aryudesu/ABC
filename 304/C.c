#include <stdio.h>
#define NMAX 2001

int root[NMAX], rank[NMAX];

void init() {
    int i;
    for (i = 0; i < NMAX; i++) {
        root[i] = -1;
        rank[i] = 0;
    }
}

int find(int x) {
    if (root[x] < 0)
        return x;
    return find(root[x]);
}

void unite(int a, int b) {
    int x, y;
    x = find(a);
    y = find(b);
    if (x == y){
        return;
    }
    if (rank[x] > rank[y]) {
        rank[x] += rank[y];
        root[y] = x;
        return;
    }
    rank[y] += rank[x];
    root[x] = y;
    if (rank[x] == rank[y])
        rank[y] += 1;
}

int same(int x, int y) {
    return find(x) == find(y);
}

int social_distance(int x1, int x2, int y1, int y2, int d) {
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) <= d * d;
}

int main() {
    int N, D, D2;
    int X[NMAX], Y[NMAX];
    int idx, idx2;

    init();

    if(scanf("%d %d", &N, &D) != 2) return 0;
    D2 = D * D;
    for (idx = 0; idx < N; idx++) {
        if(scanf("%d %d", &X[idx], &Y[idx]) != 2) return 0;
    }
    for (idx = 0; idx < N; idx++) {
        for (idx2 = 0; idx2 < N; idx2++) {
            if (idx == idx2)
                continue;
            if (social_distance(X[idx], X[idx2], Y[idx], Y[idx2], D)) {
                unite(idx, idx2);
            }
        }
    }
    for (idx = 0; idx < N; idx++)
        printf(same(0, idx)? "Yes\n" : "No\n");
    return 0;
}