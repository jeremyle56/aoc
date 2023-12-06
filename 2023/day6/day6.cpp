#include "../utils.h"

// Parses the times and distances to integers
// Many different ways to parse input
vector<pii> parseInput(vector<string> &lines) {
    vector<pii> input;

    string time = lines[0].substr(lines[0].find_first_of("0123456789"));
    string dist = lines[1].substr(lines[1].find_first_of("0123456789"));

    istringstream iss(time);
    istringstream iss1(dist);

    int number, number1;
    while (iss >> number && iss1 >> number1) {
        input.pb(make_pair(number, number1));
    }

    return input;
}

// Uses quadratic formula to calculate the number of ways
ll numWays(ll time, ll dist) {
    ll discrim = (ll)sqrt(pow(time, 2) - 4 * dist);
    ll hi = (time + discrim) / 2;
    ll lo = (time - discrim) / 2;

    return hi - lo + 1;
}

///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////

// Part 1 Solution
void solve_p1(vector<string> &lines) {
    vector<pii> input = parseInput(lines);

    int res = 1;

    for (auto race : input) {
        res *= numWays(race.first, race.second);
    }

    cout << "Answer for Part 1: " << res << endl;
}

///////////////////////////////////////////////////////////////////////////////

// Part 2 Solution
void solve_p2(vector<string> &lines) {
    regex re("[^0-9]");
    ll time = stoull(regex_replace(lines[0], re, ""));
    ll dist = stoull(regex_replace(lines[1], re, ""));

    cout << "Answer for Part 2: " << numWays(time, dist) << endl;
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