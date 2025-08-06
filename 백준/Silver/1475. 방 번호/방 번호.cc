#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    
    int arr[10] = {};
    //0에서 9까지 적힌 숫자 세트가 있는데 6과 9는 뒤집어서 쓸 수 있음
    //n을 만들려면 세트가 몇개 필요한지 구하는 문제임
    //리스트로 문자열 만드는게 제일 괜찮아 보인다.
    
    string num = to_string(n);
    for(char c : num) arr[c - '0']++;
    
    int six_nine = arr[6] + arr[9];
    arr[6] = (six_nine + 1) / 2;  // 올림 처리
    arr[9] = 0;  // 9는 6에 합쳐졌으므로 0으로 처리
    
    int answer = 0;
    for(int i = 0; i < 10; i++){
        if (arr[i] > answer)
            answer = arr[i];
    }
    cout << answer;
}