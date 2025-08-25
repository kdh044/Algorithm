#include <bits/stdc++.h>
using namespace std;

int main(void){
    int n,m;
    cin >> n >> m;
    vector <int> a;
    
    for(int i = 1; i <= n; i ++){
        if(n % i == 0){
            a.push_back(i);
        }
    }
    if(a.size() >= m) cout << a[m - 1];
    else cout << 0;
}