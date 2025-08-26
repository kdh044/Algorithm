#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int board[52][52];
bool vis[52][52];

int m , n , k;
queue <pair<int,int>> q;

void bfs(int row, int col){
    vis[row][col] = true;
    q.push({row,col});
    while(!q.empty()){
        auto cur = q.front(); q.pop();
        for(int dir = 0; dir < 4; dir++){
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];
            if(nx < 0 or nx >= n or ny < 0 or ny >= m) continue;
            if(vis[nx][ny] or !board[nx][ny]) continue;
            vis[nx][ny] = true;
            q.push({nx,ny});
        }
    }
}
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin >> t;
    
    while (t--){
        cin >> m >> n >> k;
        for(int i = 0; i < n; i++){
            fill(board[i],board[i] + m, 0);
            fill(vis[i], vis[i] + m, false);
        }
        int row, col;
        for(int i = 0; i < k; i++){
            cin >> col >> row;
            board[row][col] = 1;
        }
        int res = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(board[i][j] == 1 and !vis[i][j]){
                    bfs(i,j);
                    res++;
                }
            }
        }
            cout << res << '\n';
    }
 }
