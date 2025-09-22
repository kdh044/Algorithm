#include <bits/stdc++.h>
using namespace std;

int n;
int board[130][130];
int paper[2]; //paper[0] = white , paper[1] = blue 겠지

bool check(int x, int y, int z){
    for(int i = x; i < x + z; i++){
        for(int j = y; j < y + z; j++){
            if(board[x][y] != board[i][j]) return 0;
        }
    }return 1;
}
void cutter(int x,int y,int z){
    if(check(x,y,z)){
        paper[board[x][y]]++;  //아 맞네 어렵게 생각할게 아니구나 ㅅㅂ...
        return; 
    }
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++) cutter(x +  i * z / 2, y + j * z / 2, z / 2);
    }
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
    
    cutter(0,0,n);
    cout << paper[0] << "\n" << paper[1];
}