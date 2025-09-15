#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n = 0;
    int jinju_price;
    cin >> n;
    vector <pair<string,int>> city(n);
    for(int i = 0; i < n; i++){
        cin >> city[i].X >> city[i].Y;
        if(city[i].X == "jinju") {
            cout << city[i].Y;
            jinju_price = city[i].Y;
    }
}
    cout << "\n";
    int count = 0;
    for(int i = 0; i < n; i++){
        if (city[i].Y > jinju_price) count++; 
    }
    cout << count;
}