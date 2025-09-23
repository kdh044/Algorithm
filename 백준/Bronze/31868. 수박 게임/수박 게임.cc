#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n, k;
    
    cin >> n >> k;
    int fruit[n + 2];
    fruit[1] = k;
    for(int i = 2; i < n + 1; i++){
        fruit[i] = fruit[i - 1] / 2;
    }
    cout << fruit[n];
}