#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    while(true){
        cin >> s;
        if(s == "#") break;
        
        char parity = s.back();
        s.pop_back();
        
        int count1 = count(s.begin(), s.end(),'1');
        char lastbit;
        
        if(parity == 'e') lastbit = (count1 % 2 == 0) ? '0'  : '1';
        else lastbit = (count1 % 2 == 0) ? '1' : '0';
        
        s.push_back(lastbit);
        cout << s << '\n';
     }
}