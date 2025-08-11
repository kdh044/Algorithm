#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n);  

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // 내림차순 정렬
    sort(a.begin(), a.end());

    // 출력
    for (int x : a) {
        cout << x << '\n';
    }
}
