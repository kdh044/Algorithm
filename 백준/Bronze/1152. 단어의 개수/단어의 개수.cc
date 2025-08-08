#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string str;
    getline(cin, str);
    
    bool inworld = false;
    int ans = 0;
    for(auto c : str){
        if (c != ' ' and !inworld){
            inworld = true;
            ans++;
        }
        else if (c == ' ')inworld = false;
    }
    cout << ans;
}