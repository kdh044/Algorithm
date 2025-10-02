#include <bits/stdc++.h>
using namespace std;
int n,s,answer = 0;
int arr[22];
void check(int x, int y){
    if(x == n){
        if(y == s) answer++;
        return;
    }
    check(x + 1, y);
    check(x + 1, y + arr[x]);
}
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n >> s;
    
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    
    check(0,0);
    if(s == 0) answer--;
    
    cout << answer;
    
}