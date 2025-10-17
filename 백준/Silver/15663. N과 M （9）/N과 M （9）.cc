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
    
    int last = 0;
    
    for(int i = 0; i < n; i++){
        if(!visited[i] and num[i] != last){
            visited[i] = true;
            arr[k] = num[i];
            last = num[i];
            check(k + 1);
            visited[i] = false;
        }
    }
}
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    cin >> n >> m;
    for(int i = 0; i < n; i++) cin >> num[i];
    sort(num, num + n);
    
    check(0);

}