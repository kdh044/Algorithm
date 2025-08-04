#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N, Y, M;
    cin >> N;
    vector<int> phone(N);
    Y = 0;
    M = 0;
    for (int i = 0; i < N; i++) cin >> phone[i];
    for (int i = 0; i < N; i++){
        Y += (phone[i]/30 + 1) * 10;
        M += (phone[i]/60 + 1) * 15;
    }
    if (Y < M) cout << "Y " << Y;
    else if(M < Y) cout << "M " << M;
    else cout << "Y M " << M;
}