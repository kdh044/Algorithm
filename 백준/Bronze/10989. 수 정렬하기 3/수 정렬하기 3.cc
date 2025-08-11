#include <bits/stdc++.h>
using namespace std;
int countArr[10001];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        countArr[x]++; 
    }

    for (int i = 1; i <= 10000; i++) {
        while (countArr[i] > 0) {
            cout << i << '\n';
            countArr[i]--;
        }
    }
}
