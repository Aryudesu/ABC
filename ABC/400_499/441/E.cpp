#include <bits/stdc++.h>
using namespace std;

template <class Abel> struct BIT {
    const Abel UNITY_SUM = 0;                       // to be set
    vector<Abel> dat;
    
    /* [1, n] */
    BIT(int n) : dat(n + 1, UNITY_SUM) { }
    void init(int n) { dat.assign(n + 1, UNITY_SUM); }
    
    /* a is 1-indexed */
    inline void add(int a, Abel x) {
        for (int i = a; i < (int)dat.size(); i += i & -i)
            dat[i] = dat[i] + x;
    }
    
    /* [1, a], a is 1-indexed */
    inline Abel sum(int a) {
        Abel res = UNITY_SUM;
        for (int i = a; i > 0; i -= i & -i)
            res = res + dat[i];
        return res;
    }
    
    /* [a, b), a and b are 1-indexed */
    inline Abel sum(int a, int b) {
        return sum(b - 1) - sum(a - 1);
    }
    
    /* debug */
    void print() {
        for (int i = 1; i < (int)dat.size(); ++i) cout << sum(i, i + 1) << ",";
        cout << endl;
    }
};

int main() {
    int N;
    long long K;
    
    cin >> N >> K;
    vector<long long> S(N+1, 0);
    for (int i = 0; i < N; ++i) {
        long long a;
        cin >> a;
        S[i+1] = S[i] + (a - K);
    }
    vector<long long> SS = S;
    sort(SS.begin(), SS.end());
    SS.erase(unique(SS.begin(), SS.end()), SS.end());
    long long res = 0;
    BIT<long long> bit(N+10);
    for (int i = 0; i <= N; ++i) {
        int id = lower_bound(SS.begin(), SS.end(), S[i]) - SS.begin();
        res += bit.sum(id+1);
        bit.add(id+1, 1);
    }
    cout << res << endl;
}
