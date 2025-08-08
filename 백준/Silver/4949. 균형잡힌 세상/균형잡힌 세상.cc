#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    while (true) {
        string s;
        getline(cin, s);
        if (s == ".") break;

        deque<char> st;
        bool isValid = true;

        for (char c : s) {
            if (c == '(' or c == '[' or c == '{') {
                st.push_back(c);
            } else if (c == ')' or c == ']' or c == '}') {
                if (st.empty()) { isValid = false; break; }
                char t = st.back();
                if ((c == ')' and t != '(') ||
                    (c == ']' and t != '[') ||
                    (c == '}' and t != '{')) {
                    isValid = false; break;
                }
                st.pop_back();
            }
        }

        if (!st.empty()) isValid = false;

        cout << (isValid ? "yes" : "no") << '\n';
    }
    return 0;
}
