#include <bits/stdc++.h>
using namespace std;
int n;
int board[66][66];

bool check(int x, int y, int z){
for(int i = x; i < x + z; i++){
        for(int j = y; j < y + z; j++){
            if(board[i][j] != board[x][y]) return 0;
        }
}
    return 1;
 
}
void cutter(int x,int y, int z){
    if(check(x,y,z)) {
        cout << board[x][y]; 
        return;
    }
    
    cout << "(";
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            cutter(x + i * z / 2 , y + j * z / 2, z/2);
        }
      }
    cout << ")";
        
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    
    char c;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> c;
            board[i][j] = c - '0';
        }
    }
    cutter(0,0,n);
}