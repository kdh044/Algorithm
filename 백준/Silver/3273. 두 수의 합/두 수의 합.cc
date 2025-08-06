#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
   
    int n, x, cnt = 0;
    cin >> n;
    vector<int> a(n);
    for(int i=0; i<n; ++i) cin >> a[i];
    cin >> x;
    
    sort(a.begin(), a.end());
    
    int left = 0, right = n - 1;
    while (left < right) {
        int sum = a[left] + a[right];
        if (sum == x) {
            cnt++;
            left++;
            right--;
        }
        else if (sum < x) left++;
        else right--;
    }
    
    cout << cnt << "\n";
}