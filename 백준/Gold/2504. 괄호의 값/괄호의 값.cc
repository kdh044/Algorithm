#include <bits/stdc++.h>
using namespace std;
  
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string str;
    cin >> str;
    stack<char> s;

    int sum = 0, num = 1;
    int n = (int)str.size();

    for (int i = 0; i < n; i++) {
        if (str[i] == '(') {
            num *= 2;
            s.push('(');
        } else if (str[i] == '[') {
            num *= 3;
            s.push('[');
        } else if (str[i] == ')') {
            if (s.empty() || s.top() != '(') {
                cout << 0;
                return 0;
            }
            if (i > 0 && str[i - 1] == '(') sum += num;
            s.pop();
            num /= 2;
        } else if (str[i] == ']') {
            if (s.empty() || s.top() != '[') {
                cout << 0;
                return 0;
            }
            if (i > 0 && str[i - 1] == '[') sum += num;
            s.pop();
            num /= 3;
        } else {
  
            cout << 0;
            return 0;
        }
    }

    if (s.empty()) cout << sum;
    else cout << 0;
}