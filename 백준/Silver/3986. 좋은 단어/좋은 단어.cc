#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n , ans = 0;
    cin >> n;
    while (n--){
        stack <char> str;
        string s;
        cin >> s;
        for(auto c : s){
            if(!str.empty() and str.top() == c) str.pop();
            else(str.push(c));
        }
        if (str.empty()) ans++;
    }
    cout << ans;
}