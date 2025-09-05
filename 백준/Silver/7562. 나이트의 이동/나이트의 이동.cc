#include <bits/stdc++.h>
using namespace std;
int dist[305][305];
#define X first
#define Y second
int dx[8] = {1, 2, 2, 1, -1, -2, -2, -1};
int dy[8] = {-2, -1, 1, 2, 2, 1, -1, -2};
int n, l, x_1, y_1, x_2, y_2;
queue <pair<int,int>> Q;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n;
    while(n--){
        cin >> l;
        for(int i = 0; i < l; i++) fill(dist[i], dist[i] + l, -1);
        cin >> x_1 >> y_1;
        dist[x_1][y_1] = 0;
        Q.push({x_1,y_1});
        cin >> x_2 >> y_2;
        while(!Q.empty()){
            auto cur = Q.front(); Q.pop();
            for(int dir = 0; dir < 8; dir++){
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];
                if(nx < 0 or ny < 0 or nx >= l or ny >= l) continue;
                if(dist[nx][ny] >= 0) continue;
                dist[nx][ny] = dist[cur.X][cur.Y] + 1;
                Q.push({nx,ny});
            }
        } cout << dist[x_2][y_2] << "\n";
    } 
}