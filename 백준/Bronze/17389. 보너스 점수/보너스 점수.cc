#include <iostream>
using namespace std;

int main() {
    int n, score = 0, bonus = 0;
    string s;
    cin >> n >> s;

    for (int i = 1; i < n + 1; i++) {
        if (s[i - 1] == 'O') {
            score += (i + bonus);
            bonus++;
        } else {
            bonus = 0;
        }
    }
    cout << score;
    return 0;
}
