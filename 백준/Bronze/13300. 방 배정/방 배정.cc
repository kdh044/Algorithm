#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n, cap ,gen;
    
    cin >> n >> cap;
    
    vector<vector<int>> room(2, vector<int>(7));
    
    for(int i = 0; i < n; i++){
        int a,b;
        cin >> a >> b;
        room[a][b]++;
    }
    int ans = 0;
    for(int i = 0; i < 2; i++){
        for(int j = 1; j < 7; j++){
            ans += room[i][j]/cap;
            if (room[i][j] % cap) ans++;
        }
    } cout << ans;
}