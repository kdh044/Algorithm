#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
     if (!(cin >> T)) return 0;

    while (T--) {
        string p; int n;
        cin >> p >> n;
        string arr; cin >> arr;

        deque<int> dq;
        string num;
        
        for (char c : arr) {
            if (isdigit(c)) num += c;
            else {
                if (!num.empty()) {
                    dq.push_back(stoi(num));
                    num.clear();
                }
            }
        }

        bool rev = false;
        bool error = false;

        for (char c : p) {
            if (c == 'R') {
                rev = !rev; // 뒤집힘 상태만 토글
            } else { // 'D'
                if (dq.empty()) {
                    cout << "error\n";
                    error = true;
                    break;
                }
                if (!rev) dq.pop_front();
                else dq.pop_back();
            }
        }
        if (error) continue;

        cout << '[';
        if (!dq.empty()) {
            if (!rev) {
                for (size_t i = 0; i < dq.size(); ++i) {
                    if (i) cout << ',';
                    cout << dq[i];
                }
            } else {
                for (size_t i = 0; i < dq.size(); ++i) {
                    if (i) cout << ',';
                    cout << dq[dq.size() - 1 - i];
                }
            }
        }
        cout << "]\n";
    }
    return 0;
}