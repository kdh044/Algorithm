#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int a,b,c;
    cin >> a >> b >> c;
    
    if (a == b and b == c){
        cout << 10000 + 1000 * b;
    }
    else if (a == b or a == c){
        cout << 1000 + a * 100;
    }
    else if (b == c){
        cout << 1000 + b * 100;
    }
    else{
        cout << max({a,b,c}) * 100;
    }
}