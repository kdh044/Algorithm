#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    //(A × B) % M = ((A % M) × (B % M)) % M
    long long n,b;
    cin >> n >> b;
    
    long long result = 1;
    vector<long long> arr(n);
    for(int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < n; i++) {
        result = (result * (arr[i] % b) % b);
    }
    cout << result;
}