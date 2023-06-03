int main() {
    int N, idx, min_idx = 0;
    int A[100];
    char S[100][10];
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
