#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    
    for(int i = 0; i < n; i++){
        for(int k = 0; k < i + 1; k++) cout << "*";
        for(int j = 0; j < (n - i) * 2 - 2; j++) cout << " ";
        for(int z = 0; z < i + 1; z++) cout << "*";
        
    cout << "\n";    
    }
    
    for(int i = 0; i < n - 1; i++){
        for(int k = 0; k < n - i - 1; k++) cout << "*";
        for(int j = 0; j < 2 * (i + 1); j++) cout << " ";
        for(int z = 0; z < n - i - 1; z++) cout << "*";
        
    cout << "\n";    
    }
}