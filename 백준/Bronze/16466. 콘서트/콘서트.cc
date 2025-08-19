#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int a;
    cin >> a;
    vector <int> b;
    
    for(int i = 0; i < a; i++){
        int c;
        cin >> c;
        b.push_back(c);
    }
    
    sort(b.begin(),b.end());
    
    if (b[0] != 1){
        cout << 1; return 0;
    }
    
    for(int i = 0; i < a ; i++){
        if (b[i] + 1 != b[i+1]){
            cout << b[i] + 1; break;
        }
    }
}