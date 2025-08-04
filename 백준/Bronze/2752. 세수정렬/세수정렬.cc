#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int a, b, c, d, e, f;
    cin >> a >> b >> c;
    d = max({a,b,c});
    f = min({a,b,c});
    e = a + b + c - d - f;
    cout << f <<' '<< e << ' ' << d;
    
}