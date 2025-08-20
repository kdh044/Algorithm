#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second 
int board[501][501];
bool vis[501][501];
int n,m;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n >> m;
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> board[i][j];
        }
    }
    int mx = 0;
    int num = 0;
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(board[i][j] == 0 or vis[i][j]) continue;
            num++;
            queue<pair<int,int>> Q;
            vis[i][j] = 1;
            Q.push({i,j});
            int area = 0;
            while(!Q.empty()){
                area++;
                pair<int,int> cur = Q.front(); Q.pop();
                for(int dir = 0; dir < 4; dir++){
                    int nx = cur.x + dx[dir];
                    int ny = cur.y + dy[dir];
                    if(nx < 0 or nx >=n or ny < 0 or ny >= m) continue;
                    if(vis[nx][ny] or board[nx][ny] != 1) continue;
                    vis[nx][ny] = 1;
                    Q.push({nx,ny});
                }
            }
            mx = max(mx,area);
    }
       
}     
    cout << num << '\n' << mx;
}