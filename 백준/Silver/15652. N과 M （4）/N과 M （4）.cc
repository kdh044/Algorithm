#include <bits/stdc++.h>
using namespace std;
int n, m;
int arr[10];

void check (int x, int st){
    if(x == m){
        for(int i = 0; i < m; i++){
            cout << arr[i] << " ";
        }cout << "\n";
        return ;
    }
    

    for(int i = st; i <= n; i++){
        arr[x] = i;
        check(x + 1 , i);
    }
}
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    check(0,1);
}