#include <bits/stdc++.h>
using namespace std;

int main(void){
     ios::sync_with_stdio(0);
     cin.tie(0);
    
    int ax,ay,az,bx,by,bz,cx,cy,cz;
    
    cin >> ax >> ay >> az;
    cin >> cx >> cy >> cz;
    
    cout << cx - az << ' ' << cy / ay << ' ' << cz - ax;
    
}