#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n , m;
    
    cin >> n >> m;
    
    int num = 1; 
    
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            cout << num++;
            if (j < m)
            cout << " ";
        }
        cout << "\n";
    }
}