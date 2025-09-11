#include <bits/stdc++.h>
using namespace std;
vector<int> ve[1002];
int visita[1002];

int n, m ,t;

void dfs(int k){
    stack<int>q;
    q.push(k);
    while(!q.empty()){
        auto a = q.top(); q.pop();
        if(visita[a]) continue;
        visita[a] = 1;
        cout << a << " ";
        for(int i = ve[a].size() - 1; i >= 0; i--){
            int next = ve[a][i];
            if(!visita[next]) q.push(next);
        }
    }
}

void bfs(int k){
    queue<int>q;
    q.push(k); 
    visita[k] = 1;
    while(!q.empty()){
        auto a = q.front(); q.pop();
        visita[a] = 1;
        cout << a << " ";
        for(auto i : ve[a]){
            if(!visita[i]){
                q.push(i);
                visita[i] = 1;
            }
        }
    }
}
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m >> t;
    
    for(int i = 0; i < m; i++){
        int u, v;
        cin >> u >> v;
        ve[u].push_back(v);
        ve[v].push_back(u);
    }
    for(int j = 1; j <= n; j++) sort(ve[j].begin(), ve[j].end());
    
    dfs(t);
    
    for(int i = 1; i <= n; i++) visita[i] = 0;
    cout << "\n";
    bfs(t);
}