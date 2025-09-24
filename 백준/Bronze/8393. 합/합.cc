#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n, ans;
    
    cin >> n;
    ans = 0;
    for(int i = 1; i <= n; i++){
        ans += i;
    }
    cout << ans; //나는 병신인가?
}