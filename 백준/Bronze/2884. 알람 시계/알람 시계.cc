#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string str;
    int h,m;
    cin >> h >> m ;
    
    if(m >= 45) m = m - 45;
    else{
        m = m + 15;
        h = (h - 1 + 24) % 24;
    }
    cout << h <<" "<< m;
}
