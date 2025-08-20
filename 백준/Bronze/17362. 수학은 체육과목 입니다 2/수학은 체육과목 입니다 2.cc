#include <bits/stdc++.h>
using namespace std;

int main(void){
     ios::sync_with_stdio(0);
     cin.tie(0);
    
    int n;
    cin >> n;
    
    vector<int> pattern = {1,2,3,4,5,4,3,2};
    
    cout << pattern[(n - 1) % 8];
}