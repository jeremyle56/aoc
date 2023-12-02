#include <bits/stdc++.h>
using namespace std;

#define ll long long

#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl

#define pb push_back

#define all(x) x.begin(), x.end()
#define sortAll(x) sort(all(x))

const string INPUT_FILE_NAME = "input.txt";

// Reads file from input files into a vector
static bool readFile(vector<string> &lines) {
    ifstream file(INPUT_FILE_NAME);
    if (!file) {
        cerr << "Cannot open file" << INPUT_FILE_NAME << endl;
        return false;
    }

    string line;
    while (getline(file, line)) {
        lines.push_back(line);
    }

    file.close();
    return true;
}

///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////

// Part 1 Solution
void solve_p1(vector<string> &lines) {
    int res = 0;

    cout << "Answer for Part 1:" << res << endl;
}

///////////////////////////////////////////////////////////////////////////////

// Part 2 Solution
void solve_p2(vector<string> &lines) {
    int res = 0;

    cout << "Answer for Part 2:" << res << endl;
}

///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////

// Main function
int main() {
    vector<string> lines;
    if (!readFile(lines)) {
        return EXIT_FAILURE;
    }

    solve_p1(lines);
    solve_p2(lines);
    return EXIT_SUCCESS;
}