#include <stdio.h>
#define diff(a, b) (a<b? b-a:a-b)
#define N_MAX 500000

int main() {
    int n;
    int i, idx, count;
    unsigned long long tmp, result = 0;
    int memo[N_MAX];
    char s[N_MAX + 1];
    scanf("%d", &n);
    scanf("%s", s);
    for (i = count = 0; i < n; i++){
        if (s[i] == '0') {
            memo[count] = i;
            count++;
        }
    }
    for (i = 0; i < count; i++)
        result += diff(memo[i], i);
    tmp = result;
    for (i = 0; i < count; i++) {
        tmp -= diff(memo[count - i - 1], (count - i - 1));
        tmp += diff(memo[count - i - 1], (n - i - 1));
        result = tmp<result?tmp:result;
    }
    printf("%lld\n", result);
    return 0;
}
