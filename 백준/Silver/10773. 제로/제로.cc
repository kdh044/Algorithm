#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    stack <int> arr;
    while(n--){
        int x;
        cin >> x;
        
        if(x == 0) arr.pop();
        else arr.push(x);
    }
    int res = 0;
    
    while(!arr.empty()){
        res += arr.top();
        arr.pop();
    }
    
    cout << res;
}