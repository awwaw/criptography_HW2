//
// Created by aww on 12.05.2024.
//

#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <cmath>
#include <queue>
#include <algorithm>
#include <map>

#define print(i) cout << i << endl
#define pb push_back
#define mp make_pair

#define INF 1000000000

using namespace std;

int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

void find_all_divisors(int n, vector<int>& divs) {
    for (int i = 1; i * i <= n; i++) {
        if (i * i == n) {
            divs.pb(i);
        } else {
            if (n % i == 0) {
                divs.pb(i);
                divs.pb(n / i);
            }
        }
    }
}

int powmod(int x, int p, int m) {
    if (p == 0) {
        return 1;
    }
    if (p % 2 == 1) {
        return (powmod((x * x) % m, p / 2, m) * x) % m;
    }
    return powmod((x * x) % m, p / 2, m);
}

int primitive(int p, int g) {
    vector<int> divs;
    find_all_divisors(p - 1, divs);
    sort(divs.begin(), divs.end());
    int prev = 0;
    int s = 1;
    for (int d : divs) {
        int diff = powmod(g, d - prev, p);
        s = (s * diff) % p;
        if (s == 1) {
            return d;
        }
        prev = d;
    }
    return p - 1;
}

bool is_primitive(int p, int g) {
    return primitive(p, g) == p - 1;
}

int brute_force(int p, int g, int a, bool prime = false) {
    int tmp_pow = 1;
    for (int i = 0; i < p; i++) {
        tmp_pow = (tmp_pow * g) % p;
        if (tmp_pow == a) {
            return i + 1;
        }
    }
    return -1;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}
