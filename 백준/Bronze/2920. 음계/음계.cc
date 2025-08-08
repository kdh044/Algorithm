#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int  c ,d ,e ,f, g ,a, b, C;
    cin >>  c  >> d >> e >> f >> g >> a >> b >> C;
    
    if(c - d == 1 and d - e == 1 and e - f == 1 and f - g == 1 and g - a ==1 and a - b == 1 and b - C == 1){
        cout <<"descending";
    }
    else if(c - d == -1 and d - e == -1 and e - f == -1 and f - g == -1 and g - a == -1 and a - b == -1 and b - C == -1){
        cout <<"ascending";
    }
    else{
        cout <<"mixed";
    }
}