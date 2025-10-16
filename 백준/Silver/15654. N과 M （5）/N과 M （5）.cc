#include <bits/stdc++.h>
using namespace std;

int n, m;
int num[10];        // 입력 배열
int arr[10];        // 현재 순열 저장
bool used[10];      // 사용 여부 체크

void dfs(int x) {
    if (x == m) {
        for (int i = 0; i < m; i++) cout << arr[i] << " ";
        cout << "\n";
        return;
    }

    for (int i = 0; i < n; i++) {
        if (used[i]) continue; // 이미 사용한 수는 건너뜀
        used[i] = true;
        arr[x] = num[i];
        dfs(x + 1);
        used[i] = false;      // 재귀 종료 후 되돌리기
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> num[i];

    sort(num, num + n);  // 사전 순 출력을 위해 정렬
    dfs(0);
}
