#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    long long a, b,start, end;
    cin >> a >> b;
    end = max(a,b) - 1;
    start = min(a,b) + 1;
    if (start > end ){
        cout << 0 << "\n" << ""; 
        return 0;}
    cout << max(a,b) - min(a,b) - 1 << "\n";
    for(long long i = start; i <= end; i++)
        cout << i << " ";
    
}