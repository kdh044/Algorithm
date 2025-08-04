#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int a[9] , total , result[7];
    
    for(int i = 0; i < 9; i++) cin >> a[i];
    
    for(int i = 0; i < 8; i++){
        for(int j = i + 1; j < 9; j++){
            total = 0;
        
        for(int c = 0, d = 0; c < 9; c++) if (c != i and c != j) result[d++] = a[c];
        for(int i = 0; i < 7; i++) total += result[i];
        if (total == 100) break;
    }if (total == 100) break;
    }
    sort(result , result + 7);
    for(int i = 0; i< 7; i++) cout << result[i] <<"\n";
    
    
}
