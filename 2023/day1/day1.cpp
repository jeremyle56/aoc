#include <bits/stdc++.h>
using namespace std;

#define ll long long

#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl
#define print(x) \
    for (auto i : x) cout << i << ' ';

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

// Part 1 Solution
void solve_p1(vector<string> &lines) {
    vector<int> res;

    for (const auto &line : lines) {
        string first = line.substr(line.find_first_of("0123456789"), 1);
        string last = line.substr(line.find_last_of("0123456789"), 1);
        res.push_back(stoull(first + last));
    }

    cout << "Answer for Part 1: " << accumulate(all(res), 0) << endl;
}

// Part 2 Solution
void solve_p2(vector<string> &lines) {
    vector<int> res;

    vector<string> numbers = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    for (auto &line : lines) {
        vector<int> digits = {};
        for (size_t i = 0; i < line.length(); ++i) {
            if (isdigit(line[i])) digits.push_back(line[i] - '0');

            for (size_t j = 0; j < numbers.size(); ++j) {
                if (line.substr(i, numbers[j].length()) == numbers[j]) {
                    digits.push_back(j + 1);
                }
            }
        }

        res.push_back(digits.front() * 10 + digits.back());
    }

    cout << "Answer for Part 2: " << accumulate(all(res), 0) << endl;
}

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