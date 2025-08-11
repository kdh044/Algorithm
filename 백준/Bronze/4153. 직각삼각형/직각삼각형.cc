#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int a , b , c;
    
    while(true){
        cin >> a >> b >> c;
        if (a == 0) break;
        int arr[3] = {a,b,c};
        sort(arr,arr + 3);
        if(arr[2] * arr[2] == arr[1] * arr[1] + arr[0] * arr[0]) cout << "right\n";
        else cout << "wrong\n";
    }
}