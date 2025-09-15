#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    vector<pair<int,int>> A(4);
    
    int max_val = INT_MIN;
    int p = 0;
    
    for(int i = 0; i < 4; i++){
        cin >> A[i].X >> A[i].Y;
        p = p + A[i].Y - A[i].X;
        max_val = max(max_val,p);
    }
    cout << max_val;
    
}