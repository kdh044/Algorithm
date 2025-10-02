#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    double a , b, c;
    
    cin >> a >> b >> c;
    
    cout << max(int(a * b / c), int(a / b * c));
}