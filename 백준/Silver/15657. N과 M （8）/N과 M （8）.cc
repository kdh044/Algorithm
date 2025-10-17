#include <bits/stdc++.h>
using namespace std;
int num[10];
int arr[10];
int n,m;

void check(int k, int st){
    if(k == m){
        for(int i = 0; i < m; i++){
            cout << arr[i] << " ";
        } cout << "\n";
        return;
    }
    
    for(int i = st; i < n; i++){
        arr[k] = num[i];
        check(k + 1, i);
    }
}
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> num[i];
    }
    sort(num, num + n);
    check(0,0);
}