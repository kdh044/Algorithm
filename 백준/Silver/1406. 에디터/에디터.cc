#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string initial;
    cin >> initial;

    stack<char> left, right;

    // 초기 문자열을 왼쪽 스택에 넣음 (맨 뒤 커서)
    for (char c : initial) {
        left.push(c);
    }

    int M; // 명령 개수
    cin >> M;

    while (M--) {
        char cmd;
        cin >> cmd;

        if (cmd == 'L') {
            if (!left.empty()) {
                right.push(left.top());
                left.pop();
            }
        } else if (cmd == 'D') {
            if (!right.empty()) {
                left.push(right.top());
                right.pop();
            }
        } else if (cmd == 'B') {
            if (!left.empty()) {
                left.pop();
            }
        } else if (cmd == 'P') {
            char x;
            cin >> x;
            left.push(x);
        }
    }

    // left 스택은 역순이므로 right 스택에 옮겨서 순서 맞춤
    while (!left.empty()) {
        right.push(left.top());
        left.pop();
    }

    // 결과 출력
    while (!right.empty()) {
        cout << right.top();
        right.pop();
    }
    cout << "\n";

    return 0;
}
