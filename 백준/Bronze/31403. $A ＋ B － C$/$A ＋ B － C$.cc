#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string str;
    int a,b,c;
    cin >> a >> b >> c;
    cout << a + b - c << "\n";
    string tmp = to_string(a) + to_string(b);
    cout << stoi(tmp) - c << "\n";
}
