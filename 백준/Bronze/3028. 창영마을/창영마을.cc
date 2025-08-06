#include <bits/stdc++.h>
using namespace std;

int main(void){
    string s;
    cin >> s;
    
    bool cup[3] ={true, false ,false};
    for(char c : s){
        if (c == 'A') swap(cup[0],cup[1]);
        else if( c == 'B') swap(cup[1],cup[2]);
        else  swap(cup[0],cup[2]);
    }
    auto pos = find(cup, cup + 3, true); 
    cout << (pos - cup) + 1;
}