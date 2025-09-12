#include <bits/stdc++.h>
using namespace std;
const int MOD = 20000303;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    string s;
    
    cin >> s;
    int ans = 0;
    for(auto c : s){
        int digit = c - '0';
        ans = (ans * 10 + digit) % MOD;
    }
    cout << ans;
    
}