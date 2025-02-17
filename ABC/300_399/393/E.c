#include <stdio.h>
#define N_MAX 1200000

int main() {
    int n, k, m;
    int i, d, n2;
    int A[N_MAX + 1];
    int t[N_MAX + 1] = {0}, s[N_MAX + 1] = {0}, u[N_MAX + 1] = {0};
    scanf("%d", &n);
    scanf("%d", &k);
    for (i = 0; i < n; i++)
        scanf("%d", &A[i]);

    for (i = m = 0; i < n; i++)
        m = m < A[i] ? A[i] : m;

    for (i = 0; i < n; i++)
        s[A[i]]++;

    for (i = 0; i <= N_MAX; i++)
        t[i] = s[i];

    for (d = 1; d <= m; d++)
        for (n2 = 2 * d; n2 <= m; n2 += d)
            t[d] += s[n2];
    for (d = 1; d <= m; d++) {
        if (t[d] < k)
            continue;
        for (n2 = d; n2 <= m; n2 += d)
            u[n2] = u[n2] < d ? d : u[n2];
    }
    for (i = 0; i < n; i++)
        printf("%d\n", u[A[i]]);
    return 0;
}
