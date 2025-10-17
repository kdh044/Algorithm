#include <iostream>
#include <string>
using namespace std;

string sub(string a, string b) {
    string r = "";
    int c = 0;
    for (int i = a.size() - 1, j = b.size() - 1; i >= 0; i--, j--) {
        int d = a[i] - '0' - c - (j >= 0 ? b[j] - '0' : 0);
        if (d < 0) d += 10, c = 1;
        else c = 0;
        r = char(d + '0') + r;
    }
    while (r.size() > 1 && r[0] == '0') r.erase(0, 1);
    return r;
}

bool ge(string a, string b) {
    if (a.size() != b.size()) return a.size() > b.size();
    return a >= b;
}

int main() {
    string n, m, q = "", cur = "";
    cin >> n >> m;
    for (char c : n) {
        cur += c;
        while (cur.size() > 1 && cur[0] == '0') cur.erase(0, 1);
        int cnt = 0;
        while (ge(cur, m)) cur = sub(cur, m), cnt++;
        q += char(cnt + '0');
    }
    while (q.size() > 1 && q[0] == '0') q.erase(0, 1);
    cout << q << '\n' << cur << '\n';
}