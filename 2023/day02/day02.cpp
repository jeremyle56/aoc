#include <bits/stdc++.h>
using namespace std;

#define ll long long

#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl
#define print(x) \
    for (auto i : x) cout << i << ' '

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

    for (size_t i = 0; i < lines.size(); ++i) {
        auto line = lines[i];
        line = line.substr(line.find(": ") + 1, line.size());

        istringstream iss(line);
        string reveal;
        bool flag = true;

        while (getline(iss, reveal, ';')) {
            istringstream iss2(reveal);
            string instance;

            while (getline(iss2, instance, ',')) {
                instance = regex_replace(instance, regex("^ +| +$|( ) +"), "$1");
                istringstream iss3(instance);
                vector<string> data;
                string instanace2;

                while (getline(iss3, instanace2, ' ')) {
                    data.push_back(instanace2);
                }

                int number = stoull(data[0]);
                string colour = data[1];
                if ((colour == "red" && number > 12) || (colour == "green" && number > 13) || (colour == "blue" && number > 14)) flag = false;
            }
        }
        if (flag) res += (i + 1);
    }

    cout << "Answer for Part 1: " << res << endl;
}

///////////////////////////////////////////////////////////////////////////////

// Part 2 Solution
void solve_p2(vector<string> &lines) {
    int res = 0;

    for (size_t i = 0; i < lines.size(); ++i) {
        auto line = lines[i];
        line = line.substr(line.find(": ") + 1, line.size());

        istringstream iss(line);
        string reveal;
        int maxRed = 0;
        int maxGreen = 0;
        int maxBlue = 0;

        while (getline(iss, reveal, ';')) {
            istringstream iss2(reveal);
            string instance;

            while (getline(iss2, instance, ',')) {
                instance = regex_replace(instance, regex("^ +| +$|( ) +"), "$1");
                istringstream iss3(instance);
                vector<string> data;
                string instanace2;

                while (getline(iss3, instanace2, ' ')) {
                    data.push_back(instanace2);
                }

                int number = stoull(data[0]);
                string colour = data[1];

                if (colour == "red")
                    maxRed = max(number, maxRed);
                else if (colour == "green")
                    maxGreen = max(number, maxGreen);
                else if (colour == "blue")
                    maxBlue = max(number, maxBlue);
            }
        }
        res += (maxRed * maxGreen * maxBlue);
    }

    cout << "Answer for Part 2: " << res << endl;
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