#include <bits/stdc++.h>
using namespace std;

#define x first
#define y second

int dist[101][101];
int n,m;
string board[101];

int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n >> m;
    
    for(int i = 0; i < n; i++){
        cin >> board[i];
    }
    for(int i = 0; i < n; i++) fill(dist[i],dist[i] + m ,-1);
    
    queue<pair<int,int>> Q;
    Q.push({0,0});
    dist[0][0] = 1;
    while(!Q.empty()){
        auto cur = Q.front(); Q.pop();
        for(int dir = 0; dir < 4; dir++){
            int nx = cur.x + dx[dir];
            int ny = cur.y + dy[dir];
            if(nx < 0 or nx >= n or ny < 0 or ny >= m) continue;
            if(dist[nx][ny] >= 0 or board[nx][ny] == '0') continue;
            dist[nx][ny] = dist[cur.x][cur.y] + 1;
            Q.push({nx,ny});
        }
    }
    cout << dist[n - 1][m - 1];
}
        