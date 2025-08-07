#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    int cnt = 1;
    stack <int> s;
    string ans;
    
    while (n--){
        int a;
        cin >> a;
        while (cnt <= a){
            s.push(cnt++);
            ans += "+\n";
        }
        if(s.top() != a ){
            cout << "NO";
            return 0;
        }
        s.pop();
        ans += "-\n"; 
    }
    
    cout << ans;
    
    
}