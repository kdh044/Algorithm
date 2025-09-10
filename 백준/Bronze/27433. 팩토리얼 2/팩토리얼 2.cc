#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    long long n;
    cin >> n;
    long long ans;
    ans = 1;
    
    while(n--){
        ans *= (n + 1);
    }
    cout << ans;
}