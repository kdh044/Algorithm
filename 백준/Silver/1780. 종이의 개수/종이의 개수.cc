#include <bits/stdc++.h>
using namespace std;

int n;
int paper[2189][2189];
int cnt[3];

bool check(int x, int y, int z){
    for(int i = x; i < x + z; i++){
        for(int j = y; j < y + z; j++){
            if(paper[x][y] != paper[i][j])
                return false;}
    }
            return true;
}

void solve(int x, int y, int z){
    if(check(x,y,z)){
        cnt[paper[x][y] + 1] += 1;
        return;
    }
    int a = z / 3;
    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++)
            solve(x + i * a, y + j * a, a);
}
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    for(int i = 0; i < n; i++) 
        for(int j = 0; j < n; j++) 
            cin >> paper[i][j];
    solve(0,0,n);
    for (int i = 0; i < 3; i++) cout << cnt[i] << "\n";
    
}