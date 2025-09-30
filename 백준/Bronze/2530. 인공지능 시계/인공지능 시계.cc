#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int h,m,s,time;
    cin >> h >> m >> s;
    cin >> time;
    
    s += time;
    m = m + s / 60;
    s %= 60;
    h = h + m / 60;
    m %= 60;
    h %= 24;
    cout << h << " " << m << " "<< s;
}