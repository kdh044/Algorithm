#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int a,b, sum;
    sum = 0;
    cin >> a >> b;
    
    
    for(int i = 0; i < b; i++){
        int x;
        cin >> x;
        sum += x;
    }
    
if (sum >= a){
    cout << "Padaeng_i Happy";
}

else {
    cout << "Padaeng_i Cry";
}
}