#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define int ll

#define y second.first
#define z second.second

struct UF {
    vector<int> e;

    UF(int n) : e(n, -1) {}

    bool sameSet(int a, int b) { return find(a) == find(b); }

    int size(int x) { return -e[find(x)]; }

    int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }

    bool join(int a, int b) {
        a = find(a), b = find(b);
        if (a == b) return false;
        if (e[a] > e[b]) swap(a, b);
        e[a] += e[b];
        e[b] = a;
        return true;
    }
};

typedef pair<int, pair<int, int>> T;
typedef pair<int, pair<int, int>> A;

static inline ll dist(A a, A b) {
    return (ll)powl(a.first - b.first, 2) + (ll)powl(a.y - b.y, 2) + (ll)powl(a.z - b.z, 2);
}

signed main() {
    cin.tie(0)->sync_with_stdio(0);
    ifstream infile("in.txt");
    if (!infile.is_open()) {
        cerr << "Error\n";
        return 1;
    }

    vector<pair<int, pair<int, int>>> points;

    string line;
    while (getline(infile, line)) {
        replace(line.begin(), line.end(), ',', ' ');
        stringstream ss(line);

        int a, b, c;
        if (ss >> a >> b >> c) {
            points.push_back({a, {b, c}});
        }
    }

    infile.close();

    priority_queue<T, vector<T>> pq;
    int n = (int)points.size();

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            pq.push({dist(points[i], points[j]), {i, j}});
            if (pq.size() > 1000) pq.pop();
        }
    }

    struct UF uf(n);
    for (int i = 0; i < 1000; ++i) {
        T e = pq.top();
        pq.pop();
        uf.join(e.second.first, e.second.second);
    }

    vector<ll> sz;
    vector<bool> seen(n, false);
    for (int i = 0; i < n; ++i) {
        int c = uf.find(i);
        if (!seen[c]) {
            seen[c] = true;
            sz.push_back(uf.size(c));
        }
    }

    sort(sz.begin(), sz.end(), greater<>());
    cout << sz[0] * sz[1] * sz[2] << '\n';
}