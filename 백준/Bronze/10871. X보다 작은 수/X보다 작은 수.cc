#include <bits/stdc++.h>
using namespace std;

int main(){
    //파이썬이면 리스트로 정렬한다음에 반복문써서 5보다 작은수 뽑았을텐데...  C++은 구현이힘드네
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, x, a[10000];
    cin >> n >> x;
    for(int i=0; i<n; i++) cin >> a[i];
    for(int j=0; j<n; j++)
        if (a[j] < x) cout << a[j] << ' '; 
    return 0;
}