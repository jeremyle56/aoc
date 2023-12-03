#include "../utils.h"

bool isPartFunc(int i, int j, int n, int m, vector<vector<char>> &schematic) {
    if (i < 0 || j < 0 || i > n - 1 || j > m - 1)
        return false;
    return !isdigit(schematic[i][j]) && schematic[i][j] != '.';
}

bool isGearFunc(int i, int j, int n, int m, vector<vector<char>> &schematic) {
    if (i < 0 || j < 0 || i > n - 1 || j > m - 1)
        return false;
    return isdigit(schematic[i][j]);
}

string getNumber(int i, int j, int m, vector<vector<char>> &schematic) {
    for (; j > 0 && isdigit(schematic[i][j]); --j) {
    }

    if (!isdigit(schematic[i][j])) ++j;

    string number;
    for (; j < m && isdigit(schematic[i][j]); ++j) {
        number += schematic[i][j];
    }

    return number;
}

///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////

// Part 1 Solution
void solve_p1(vector<vector<char>> &schematic) {
    int sum = 0;
    int rows = schematic.size();
    int cols = schematic[0].size();

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            bool isPart = false;
            string number = "";
            for (; j < cols && isdigit(schematic[i][j]); ++j) {
                if (isPartFunc(i - 1, j - 1, rows, cols, schematic))
                    isPart = true;
                else if (isPartFunc(i - 1, j, rows, cols, schematic))
                    isPart = true;
                else if (isPartFunc(i - 1, j + 1, rows, cols, schematic))
                    isPart = true;
                else if (isPartFunc(i, j - 1, rows, cols, schematic))
                    isPart = true;
                else if (isPartFunc(i, j + 1, rows, cols, schematic))
                    isPart = true;
                else if (isPartFunc(i + 1, j - 1, rows, cols, schematic))
                    isPart = true;
                else if (isPartFunc(i + 1, j, rows, cols, schematic))
                    isPart = true;
                else if (isPartFunc(i + 1, j + 1, rows, cols, schematic))
                    isPart = true;
                number += schematic[i][j];
            }
            if (isPart) sum += stoull(number);
        }
    }

    cout << "Answer for Part 1: " << sum << endl;
}

///////////////////////////////////////////////////////////////////////////////

// Part 2 Solution
void solve_p2(vector<vector<char>> &schematic) {
    int ratio = 0;
    int rows = schematic.size();
    int cols = schematic[0].size();

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            int partCount = 0;
            vector<string> numbers;
            if (schematic[i][j] == '*') {
                if (isGearFunc(i - 1, j - 1, rows, cols, schematic) && isGearFunc(i - 1, j, rows, cols, schematic) && isGearFunc(i - 1, j + 1, rows, cols, schematic)) {
                    partCount++;
                    string num = getNumber(i - 1, j - 1, cols, schematic);
                    if (!num.empty()) numbers.pb(num);
                } else if (isGearFunc(i - 1, j - 1, rows, cols, schematic) && isGearFunc(i - 1, j, rows, cols, schematic)) {
                    partCount++;
                    string num = getNumber(i - 1, j - 1, cols, schematic);
                    if (!num.empty()) numbers.pb(num);
                } else if (isGearFunc(i - 1, j, rows, cols, schematic) && isGearFunc(i - 1, j + 1, rows, cols, schematic)) {
                    partCount++;
                    string num = getNumber(i - 1, j, cols, schematic);
                    if (!num.empty()) numbers.pb(num);
                } else {
                    if (isGearFunc(i - 1, j - 1, rows, cols, schematic)) {
                        partCount++;
                        string num = getNumber(i - 1, j - 1, cols, schematic);
                        if (!num.empty()) numbers.pb(num);
                    }
                    if (isGearFunc(i - 1, j, rows, cols, schematic)) {
                        partCount++;
                        string num = getNumber(i - 1, j, cols, schematic);
                        if (!num.empty()) numbers.pb(num);
                    }
                    if (isGearFunc(i - 1, j + 1, rows, cols, schematic)) {
                        partCount++;
                        string num = getNumber(i - 1, j + 1, cols, schematic);
                        if (!num.empty()) numbers.pb(num);
                    }
                }

                if (isGearFunc(i, j - 1, rows, cols, schematic)) {
                    partCount++;
                    string num = getNumber(i, j - 1, cols, schematic);
                    if (!num.empty()) numbers.pb(num);
                }
                if (isGearFunc(i, j + 1, rows, cols, schematic)) {
                    partCount++;
                    string num = getNumber(i, j + 1, cols, schematic);
                    if (!num.empty()) numbers.pb(num);
                }

                if (isGearFunc(i + 1, j - 1, rows, cols, schematic) && isGearFunc(i + 1, j, rows, cols, schematic) && isGearFunc(i + 1, j + 1, rows, cols, schematic)) {
                    partCount++;
                    string num = getNumber(i + 1, j - 1, cols, schematic);
                    if (!num.empty()) numbers.pb(num);
                } else if (isGearFunc(i + 1, j - 1, rows, cols, schematic) && isGearFunc(i + 1, j, rows, cols, schematic)) {
                    partCount++;
                    string num = getNumber(i + 1, j - 1, cols, schematic);
                    if (!num.empty()) numbers.pb(num);
                } else if (isGearFunc(i + 1, j, rows, cols, schematic) && isGearFunc(i + 1, j + 1, rows, cols, schematic)) {
                    partCount++;
                    string num = getNumber(i + 1, j, cols, schematic);
                    if (!num.empty()) numbers.pb(num);
                } else {
                    if (isGearFunc(i + 1, j - 1, rows, cols, schematic)) {
                        partCount++;
                        string num = getNumber(i + 1, j - 1, cols, schematic);
                        if (!num.empty()) numbers.pb(num);
                    }
                    if (isGearFunc(i + 1, j, rows, cols, schematic)) {
                        partCount++;
                        string num = getNumber(i + 1, j, cols, schematic);
                        if (!num.empty()) numbers.pb(num);
                    }
                    if (isGearFunc(i + 1, j + 1, rows, cols, schematic)) {
                        partCount++;
                        string num = getNumber(i + 1, j + 1, cols, schematic);
                        if (!num.empty()) numbers.pb(num);
                    }
                }

                if (partCount == 2) {
                    ratio += stoull(numbers[0]) * stoull(numbers[1]);
                }
            }
        }
    }
    cout << "Answer for Part 2: " << ratio << endl;
}

///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////

// Main function
int main() {
    vector<string> lines;
    if (!readFile(lines)) {
        return EXIT_FAILURE;
    }

    vector<vector<char>> schematic;
    for (auto &line : lines) {
        vector<char> row;
        for (auto c : line) {
            row.pb(c);
        }
        schematic.pb(row);
    }

    solve_p1(schematic);
    solve_p2(schematic);
    return EXIT_SUCCESS;
}