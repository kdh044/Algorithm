#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int A, B, C;
  cin >> A >> B >> C;
  int t = A * B * C;
  int d[10] = {};
  // baaaaarking dog 식 풀이 형변환 x
    while(t > 0){
        d[t % 10]++;
        t = t/10;
    }
    for(int i = 0; i< 10; i++) cout << d[i] << "\n";
    }