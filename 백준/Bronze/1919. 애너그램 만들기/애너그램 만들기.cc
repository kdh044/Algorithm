#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int arr[2][26] = {} ,res = 0;
    string a , b;
    cin >> a >> b;
    
    for(char c : a){
        arr[0][c - 'a']++;
    }
    
    for(char c : b){
        arr[1][c - 'a']++;
    }
    
    for(int i = 0; i < 26; i++)
    {
        res += abs(arr[1][i] - arr[0][i]);
    }
    cout << res;
}