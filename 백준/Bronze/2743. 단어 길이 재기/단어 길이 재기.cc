#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    
    cin >> s;
    
    int a = 0;
    for(auto c : s) a++;
    cout << a;
}