#include <bits/stdc++.h>
using namespace std;

int main(void){
    cin.tie(0);
    ios::sync_with_stdio(0);
    
    int n = 0, x;
    for(int i = 0; i < 5; i++){
        cin >> x;
        n += x;
    }
    cout << n;
}