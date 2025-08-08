#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    string s;
    cin >> s;

    int pos[26];
    for (int i = 0; i < 26; ++i) pos[i] = -1; 

    for (int i = 0; i < s.size(); ++i){
        char c = s[i];
    
    if ('a' <= c && c <= 'z'){
        int idx = c - 'a';
        if (pos[idx] == -1) pos[idx] = i;  
    }
}

    for (int i = 0; i < 26; ++i){
        if (i) cout << ' ';
        cout << pos[i];
    }
    cout << '\n';
}