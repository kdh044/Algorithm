#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    while(n--){
        string s;
        cin >> s;
        stack <char> a;
        bool ok = true;
        for(auto c : s){
            if(!a.empty() and a.top() == '(' and c == ')')
                a.pop();
            
            else if(c == '(')
                a.push(c);
            
            else{
                ok = false;
                break;
            }
        }
        if(a.empty() and ok == true){
            cout << "YES\n";
        }
        else{
            cout << "NO\n";
        }
    }
}