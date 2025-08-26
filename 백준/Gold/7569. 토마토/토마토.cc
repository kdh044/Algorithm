#include <bits/stdc++.h>
using namespace std;

int dx[6] = {0,0,1,-1,0,0};
int dy[6] = {1,-1,0,0,0,0};
int dz[6] = {0,0,0,0,1,-1};
int board[102][102][102];
int dist[102][102][102];

queue<tuple<int,int,int>> Q;
int m,n,h;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> m >> n >> h;
    for(int k = 0; k < h; k++){
        for(int j = 0; j < n; j++){
            for(int i = 0; i < m; i++){
                int tmp;
                cin >> tmp;
                board[i][j][k] = tmp;
                if(tmp == 1) Q.push({i,j,k});
                if(tmp == 0) dist[i][j][k] = -1;
            }
        }
    }
    while (!Q.empty()){
        auto cur = Q.front(); Q.pop();
        int curX, curY, curZ;
        tie(curX, curY, curZ) = cur;
        for(int dir = 0; dir < 6; dir++){
            int nx = curX + dx[dir];
            int ny = curY + dy[dir];
            int nz = curZ + dz[dir];
            if(nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h) continue;
            if(dist[nx][ny][nz] >= 0) continue;
            dist[nx][ny][nz] = dist[curX][curY][curZ] + 1;
            Q.push({nx,ny,nz});
        }
    }
    int ans = 0;
    for(int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            for(int k = 0; k < h; k++){
                if(dist[i][j][k] == -1){
                    cout << -1 << "\n";
                    return 0;
                }
                ans = max(ans,dist[i][j][k]);
            }
        }
    }
    cout << ans << "\n";
    return 0;
    
}