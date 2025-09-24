#include <bits/stdc++.h>
using namespace std;
int n;
char s[2200][2200];

void cutter(int x, int y, int z){
    if(z == 1) return;
    int div = z / 3;
    for(int i = x + div; i < x + 2 * div; i++){
        for(int j = y + div; j < y + 2 * div; j++){
            s[i][j] = ' ';
        }
    }
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            if (i == 1 and j == 1) continue;
            cutter(x + i * div , y + j * div, div);
        }
    }
}
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            s[i][j] = '*';
        }
    }
    
    cutter(0,0,n);
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << s[i][j];
        }
        cout << "\n";
    }
}