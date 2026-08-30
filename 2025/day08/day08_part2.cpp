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
vector<pair<int, pair<int, int>>> points;

static inline ll dist(A a, A b) {
    ll dx = ll(a.first) - ll(b.first);
    ll dy = ll(a.y) - ll(b.y);
    ll dz = ll(a.z) - ll(b.z);
    return dx * dx + dy * dy + dz * dz;
}

struct edge {
    int u, v, w;
};
bool operator<(const edge& a, const edge& b) { return a.w < b.w; }

vector<edge> edges;
int mst(struct UF uf) {
    sort(edges.begin(), edges.end());  // sort by increasing weight
    int res = 0;
    for (int i = 0; i < edges.size(); i++) {
        edge& e = edges[i];
        if (!uf.sameSet(e.u, e.v)) {
            uf.join(e.u, e.v);
            res = points[e.u].first * points[e.v].first;
        }
    }
    return res;
}

signed main() {
    cin.tie(0)->sync_with_stdio(0);
    ifstream infile("in.txt");
    if (!infile.is_open()) {
        cerr << "Error\n";
        return 1;
    }

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

    const int n = (int)points.size();
    struct UF uf(n);

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) edges.push_back((edge){i, j, dist(points[i], points[j])});
    }

    cout << mst(uf) << '\n';
}