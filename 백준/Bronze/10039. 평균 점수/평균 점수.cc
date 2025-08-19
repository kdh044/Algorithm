#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    vector <int> a(5);
    
    for(int i = 0; i < 5; i++){
        cin >> a[i];
    }
    
    for(int i = 0; i < 5; i++){
        if (a[i] < 40) a[i] = 40;
    }
    
    int sum = accumulate(a.begin(),a.end(),0);
    cout << sum/5;
}