#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    bool ch[42] = {false};
    
    for(int i = 0; i < 10; i++){
        int n;
        cin >> n;
        ch[n % 42] = true;
    }
    int ans = 0;
    for(int i = 0; i < 42; i++){
        if(ch[i]) ans++;
    }
    cout << ans;
}