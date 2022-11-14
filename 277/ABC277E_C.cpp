#include <stdio.h>
#define N_MAX 200000


int input(){
    /* 数値の入力を行います */
    int res;
    scanf("%d", &res);
    return res;
}


void node_init(int nodeA[N_MAX * 2], int nodeB[N_MAX * 2]){
    int i;
    for (i = 0; i < N_MAX * 2; i++){
        nodeA[i] = nodeB[i] = -1;
    }
}


int search(int num[N_MAX], int branch[N_MAX][2], int button[N_MAX], int n, int m, int k) {
    /* 幅優先探索を行います */
    int now_node[N_MAX * 2], next_node[N_MAX * 2]; // 現在位置
    int node_num = 0, next_node_num = 0; // 現在いるノード
    int result = 0; // 結果（探索のループ回数で良い
    int node, a, length;
    int f = 0;
    int i = 0;
    // ノード状態初期化
    node_init(now_node, next_node);
    // 始点
    now_node[0] = N_MAX;
    node_num = 1;
    // 最初にボタンがある場合はボタンを押した場合もノードを用意する
    if (button[0]) {
        now_node[1] = 0;
        node_num = 2;
    }
    while (true) {
        result++;
        next_node_num = 0;
        // 現在いる全てのノードに対して
        for (i = 0; i < node_num; i ++) {
            // ノード
            node = now_node[i] % N_MAX;
            // ボタンの状態
            a = now_node[i] / N_MAX;
            length = branch[node][a];
        }
        if (next_node[N_MAX - 1] > 0)
            return result;
        if (next_node[N_MAX * 2 - 1] > 0)
            return result;
        // 次のノードがなくなればゴールにたどり着けない
        if (next_node_num == 0)
            return -1;
    }
    return result;
}


void input_data(int num[N_MAX], int branch[N_MAX][2], int button[N_MAX], int n, int m, int k) {
    /* 情報を入力します */
    int i;
    int u, v, a;
    int s;
    for (i = 0; i < m; i++){
        u = input() - 1;
        v = input() - 1;
        a = input();
        branch[v][num[v]] = u;
        branch[u][num[u]] = v;
        num[v]++;
        num[u]++;
    }
    for (i = 0; i < k; i++){
        s = input() - 1;
        button[s] = 1;
    }
}

void init_data(int num[N_MAX], int branch[N_MAX][2], int button[N_MAX])
{
    /* 値を初期化します */
    int i;
    for (i = 0; i < N_MAX; i++){
        num[i] = 0;
        branch[i][0] = branch[i][1] = 0;
        button[i] = 0;
    }
    return;
}

int calc(){
    /* 計算を行います */
    int n, m, k;
    int i, j;
    int branch[N_MAX][2]; // 枝
    int num[N_MAX]; // 頂点
    int button[N_MAX];
    init_data(num, branch, button);
    n = input();
    m = input();
    k = input();
}


int main(){
    return 0;
}