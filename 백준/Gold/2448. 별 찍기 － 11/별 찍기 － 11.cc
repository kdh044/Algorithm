#include <bits/stdc++.h>
using namespace std;
const int MAX = 1024 * 3 + 2;

int n;
char board[MAX][MAX * 2 - 1];

void fill_star(int x, int y){
    board[x][y] = '*';
    board[x + 1][y - 1] = '*', board[x + 1][y + 1] = '*';
   
    for(int k = 0; k < 5; k ++)  board[x + 2][y - 2 + k] = '*';
}

void func(int s, int x,int y){
    if(s == 3){
        fill_star(x,y);
        return;
    }
    int ns = s / 2;
    func(ns, x , y);
    func(ns, x + ns, y - ns);
    func(ns, x + ns, y + ns);
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    
   func(n,0,n - 1);
   for(int i = 0; i < n; i++){
       for(int j = 0; j < n * 2 - 1; j++){
           if(board[i][j] == '*')
                   cout << '*';
               else
                   cout << " ";
           }
           cout << "\n";
       }
}