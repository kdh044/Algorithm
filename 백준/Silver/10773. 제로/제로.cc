#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    vector <int> arr;
    while(n--){
        int x;
        cin >> x;
        
        if(x == 0) arr.pop_back();
        else arr.push_back(x);
    }
    long long res = 0;
    for(auto i : arr) res += i;
    
    cout << res;
}