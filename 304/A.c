#include <stdio.h>

int main() {
    int N, idx, min_idx = 0;
    int A[101];
    char S[101][11];
    scanf("%d", &N);
    for (idx = 0; idx < N; idx++) {
        scanf("%s %d", S[idx], &A[idx]);
        if (A[idx] < A[min_idx])min_idx = idx;
    }
    for (idx = 0; idx < N; idx++) {
        printf("%s\n", S[(idx + min_idx) % N]);
    }
    return 0;
}
