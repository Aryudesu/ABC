#include <stdio.h>
#define DATA_MAX 10000001
#define MOD 998244353

int partition(int num, int data[]) {
    int result = 0, i;
    int g1, g2;
    for (i = 1; i <= num; i++) {
        g1 = (i * (3 * i - 1)) / 2;
        g2 = (i * (3 * i + 1)) / 2;
        if (num < g1 && num < g2)
            break;
        if (num >= g1)
            result += (i%2)?data[num - g1]: - data[num - g1];
        if (num >= g2) result += (i%2)?data[num - g2]: - data[num - g2];
    }
    return result;
}

int calcPartition(int num) {
    int data[DATA_MAX] = {0};
    int i;
    data[0] = 1;
    for (i = 1; i <= num; i++)
        data[i] = partition(i, data);
    return data[num];
}

int main() {
    int N, tmp;
    tmp = scanf("%d", &N);
    printf("%d\n", calcPartition(N));
    return 0;
}