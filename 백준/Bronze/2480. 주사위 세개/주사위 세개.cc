#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int a[3];
    cin >> a[0] >> a[1] >> a[2];
    sort(a, a+3);
    
    if(a[0] == a[2]){
        cout << a[0] * 1000 + 10000;
    }
    else if (a[0] == a[1] or a[1] == a[2]){
        cout << a[1] * 100 + 1000;
    }
    else
        cout << a[2] * 100;
}