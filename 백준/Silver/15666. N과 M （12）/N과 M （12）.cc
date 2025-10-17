#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[10];
int num[10];

void check(int k, int st){
    if(k == m){
        for(int i = 0; i < m; i++)
            cout << arr[i] << " ";
        cout << "\n";
        return;
    }
    int tmp = 0;
    for(int i = st; i < n; i++){
        if(num[i] != tmp){
            arr[k] = num[i];
            tmp = arr[k];
            check(k + 1, i);
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> num[i];
    }
    
    sort(num, num + n);
    check(0,0);
}
