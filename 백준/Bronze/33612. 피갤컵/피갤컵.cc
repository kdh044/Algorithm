#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    
    cin >> n;
    
    if(n == 1) cout << "2024 8";
    else if(n == 2) cout << "2025 3";
    else if(n == 3) cout << "2025 10";
    else if(n == 4) cout << "2026 5";
    else cout << "2026 12";
}