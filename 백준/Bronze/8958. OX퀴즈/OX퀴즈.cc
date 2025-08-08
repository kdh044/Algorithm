#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
 
    while (n--){
        string str;
        cin >> str;
        int ans = 0;
        int run = 0;
        for(auto c : str){
            if(c == 'O'){
                run++;
                ans += run;
            }
            else{
                run = 0;
            }
        }cout << ans << "\n";  
    }
}