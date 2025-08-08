#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    
    while (t--){
        int h,w,n;
        cin >> h >> w >> n;
        int floor, room;
        floor = (n - 1) % h + 1;
        room = (n - 1) / h + 1;
        int res = floor * 100 + room;
        cout << res << "\n";
    }


}