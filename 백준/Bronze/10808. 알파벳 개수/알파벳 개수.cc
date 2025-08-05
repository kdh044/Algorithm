#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int count[26] = {0};
    string s;
    cin >> s;
    
    for(char c : s) count[c - 'a']++;
    
    for(int i = 0; i < 26; i++) cout << count[i] << " ";
    
}