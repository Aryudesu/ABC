#include <stdio.h>
 
int get_min(int field[3001][3001], int y, int x) {
    int result;
    if (field[y][x] == -1)
        return 0;
    result = field[y - 1][x - 1];
    result = result > field[y - 1][x] ? field[y - 1][x]: result;
    result = result > field[y][x - 1] ? field[y][x - 1]: result;
    return result + 1;
}
 
 
int main(){
    int field[3001][3001] = {0};
    int h, w, H, W, N;
    unsigned long long result = 0;
    scanf("%d %d %d", &H, &W, &N);
    for (; N; N--) {
        scanf("%d %d", &h, &w);
        field[h][w] = -1;
    }
    for (h = 1; h <= H; h++) {
        for (w = 1; w <= W; w++) {
            N = get_min(field, h, w);
            field[h][w] = N;
            result += N;
        }
    }
    printf("%llu", result);
    return 0;
}