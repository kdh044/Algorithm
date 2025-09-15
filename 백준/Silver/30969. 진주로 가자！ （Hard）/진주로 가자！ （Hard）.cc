#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    long long jinju_price;
    

    int over_1000_count = 0;
    int prices_1000[1001] = {0};
    
    cin >> n;
    for(int i = 0; i < n; i++){
        string city;
        long long price;
        cin >> city >> price;
        
        if(city == "jinju") {
            jinju_price = price;
            cout << jinju_price << "\n";
        } else {
            if(price > 1000) over_1000_count++;
            else prices_1000[price]++;
        }
    }
        int count = over_1000_count;
        for(int p = jinju_price + 1; p <= 1000; p++){
            count += prices_1000[p];
        }
            cout << count;
}
