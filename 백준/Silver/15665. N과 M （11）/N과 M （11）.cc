#include <bits/stdc++.h>
using namespace std;
int n,m;
int arr[10];
int num[10];
bool visited[10];

void check(int k){
    if(k == m){
        for(int i = 0; i < m; i++){
            cout << arr[i] << " ";
        }cout << "\n";
        return;
    }
    
    for(int i = 0; i < n; i++){
        arr[k] = num[i];
        check(k + 1);
    }
}
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    cin >> n >> m;
    
    vector<bool> chk(10002);
    int idx = 0;
    for(int i = 0; i < n; i++) {
        int x; 
        cin >> x;
        if(chk[x]) continue;
        chk[x] = true;
        num[idx++] = x;
    }  
    n = idx;
    sort(num, num + n);
    check(0);

}