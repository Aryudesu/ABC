#define MAX 200000

int main() {
    int N;
    char data[MAX];
    char result[MAX];
    int idx = 0, i;
    scanf("%d", &N);
    scanf("%s", data);
    printf("%s\n", data);
    for (i = 0; i < N;i++){
        result[idx] = data[i];
    }
    return 0;
}