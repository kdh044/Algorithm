#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    
    if(n % 2024 == 0 and n <= 100000){
        cout << "Yes";
    }
    else{
        cout << "No";
    }
}