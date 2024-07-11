#include <stdio.h>


void init(int card_list[13][4]) {
    int i, j;
    for (i = 0; i < 13; i++){
        for (j = 0; j < 4; j++)
            card_list[i][j] = 0;
    }
    return;
}

int return_index(char c, char *str, int len)
{
    int i;
    for (i = 0; i < len; i++) {
        if (str[i] == c)
            return i;
    }
    return -1;
}

int calc(int n){
    int i;
    int mark, num;
    int card_list[13][4];
    char card[2];
    init(card_list);
    for (i = 0; i < n; i++){
        scanf("%s", card);
        mark = return_index(card[0], "DCHS", 4);
        num = return_index(card[1], "A23456789TJQK", 13);
        if (mark == -1 || num == -1)
            return 0;
        if (card_list[num][mark])
            return 0;
        card_list[num][mark] = 1;
    }
    return 1;
}


int main(){
    int n, result;
    scanf("%d", &n);
    result = calc(n);
    printf(result? "Yes": "No");
    return 0;
}
