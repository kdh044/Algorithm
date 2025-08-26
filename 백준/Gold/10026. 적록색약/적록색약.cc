#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
char board[102][102];
bool vis[102][102];
int n;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
void bfs(int i, int j){
    queue<pair<int,int>> Q;
    Q.push({i,j});
    vis[i][j] = 1;
    while(!Q.empty()){
        auto cur = Q.front(); Q.pop();
        for(int dir = 0; dir < 4; dir++){
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];
            if(nx < 0 or nx >= n or ny < 0 or ny >= n) continue;
            if(vis[nx][ny] or board[i][j] != board[nx][ny]) continue;
            vis[nx][ny] = 1;
            Q.push({nx,ny});
        }
    }
}

int area(){
    int cnt = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(!vis[i][j]){
                cnt++;
                bfs(i,j);
            }
        }
    }
    return cnt;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> board[i][j];
        }
    }
    int not_g = area();
    
    for(int i = 0; i < n; i++){
        fill(vis[i], vis[i] + n, false);
    }
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(board[i][j] == 'G') board[i][j] = 'R';
        }
    }
    int is_g = area();
    cout << not_g << " " << is_g;
}