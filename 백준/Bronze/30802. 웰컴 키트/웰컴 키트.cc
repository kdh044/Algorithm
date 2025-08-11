#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long n;
    cin >> n;
    
    vector<long long> tshirt(6);
    for (int i = 0; i < 6; i++) cin >> tshirt[i];

    long long T, P;
    cin >> T >> P;

    long long sum = 0;
    for (int i = 0; i < 6; i++) {
        sum += (tshirt[i] + T - 1) / T; 
    }

    cout << sum << '\n';

    cout << n / P << ' ' << n % P << '\n';
}