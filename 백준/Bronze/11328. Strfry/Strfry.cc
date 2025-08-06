#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    
    for(int i = 0; i < n; i++ ){
    string a , b;
    cin >> a >> b;
    
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    
    if(a == b) cout << "Possible\n";
    else cout << "Impossible\n";
    }
}