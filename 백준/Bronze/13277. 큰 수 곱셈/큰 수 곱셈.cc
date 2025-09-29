#include <bits/stdc++.h>
using namespace std;
using cd = complex<double>;
const double PI = acos(-1);

// FFT 함수
void fft(vector<cd> & a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1)
            j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        double ang = 2 * PI / len * (invert ? -1 : 1);
        cd wlen(cos(ang), sin(ang));
        for (int i = 0; i < n; i += len) {
            cd w(1);
            for (int j = 0; j < len/2; j++) {
                cd u = a[i+j], v = a[i+j+len/2]*w;
                a[i+j] = u+v;
                a[i+j+len/2] = u-v;
                w *= wlen;
            }
        }
    }
    if (invert) {
        for (cd & x : a) x /= n;
    }
}

// 두 큰 수 곱셈
vector<int> multiply(vector<int> const & a, vector<int> const & b) {
    vector<cd> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    int n = 1;
    while (n < a.size() + b.size()) n <<= 1;
    fa.resize(n); fb.resize(n);

    fft(fa, false); fft(fb, false);
    for (int i = 0; i < n; i++) fa[i] *= fb[i];
    fft(fa, true);

    vector<int> result(n);
    long long carry = 0;
    for (int i = 0; i < n; i++) {
        long long t = (long long)(round(fa[i].real())) + carry;
        result[i] = t % 10;
        carry = t / 10;
    }
    while (carry) {
        result.push_back(carry % 10);
        carry /= 10;
    }
    while (result.size() > 1 && result.back() == 0) result.pop_back();
    return result;
}

int main() {
    string s1, s2;
    cin >> s1 >> s2;
    reverse(s1.begin(), s1.end());
    reverse(s2.begin(), s2.end());

    vector<int> a, b;
    for (char c : s1) a.push_back(c - '0');
    for (char c : s2) b.push_back(c - '0');

    vector<int> res = multiply(a, b);
    for (int i = res.size()-1; i >= 0; i--) cout << res[i];
    cout << '\n';
    return 0;
}
