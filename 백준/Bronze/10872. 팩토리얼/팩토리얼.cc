#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    
    int a = 1;
    while(n > 1){
        a *= n;
        n--;
    }
    cout << a;
}