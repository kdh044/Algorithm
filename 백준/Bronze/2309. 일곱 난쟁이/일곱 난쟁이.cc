#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int a[9];
    int total;
    int result[7];
    
    for(int i = 0; i < 9; i++) cin >> a[i];
    
    for(int x = 0; x < 8; x++){
        total = 0;
        
        for(int y = x + 1; y < 9; y++){
            total = 0;
            
            for(int c = 0, i = 0; c < 9; c++) 
                if(c != x && c != y) 
                    result[i++] = a[c];
                    
            for(int i = 0; i < 7; i++) total += result[i];
            
            if(total == 100) break;
        }
        if(total == 100) break;
    }
    
    sort(result, result + 7);
    for(int i = 0; i < 7; i++) cout << result[i] << "\n";
}
