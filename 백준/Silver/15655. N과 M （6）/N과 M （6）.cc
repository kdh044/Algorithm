#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[10];
vector<int> nums;

void check(int k ,int y){
    if(k == m){
        for(int i = 0; i < m; i++){
            cout << arr[i] << " ";
        } cout << "\n";
        return;
    }
    
    for(int i = y; i < n; i++){
        arr[k] = nums[i];
        check(k + 1, i + 1);
    }
}
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    int x;
    set<int> s;
    for(int i = 0; i < n; i++){
        cin >> x;
        s.insert(x);
    }
    
    for(int val : s) nums.push_back(val);
    check(0 , 0);
}