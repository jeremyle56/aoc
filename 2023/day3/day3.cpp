#include "../utils.h"

// Given coordinates, checks if they are valid and symbol
bool isPartFunc(int i, int j, vector<vector<char>> &schematic) {
    int n = schematic.size();
    int m = schematic[0].size();
    if (i < 0 || j < 0 || i > n - 1 || j > m - 1) return false;
    return !isdigit(schematic[i][j]) && schematic[i][j] != '.';
}

// Given coordinates, checks if they are valid and partNumber
bool isGearFunc(int i, int j, int n, int m, vector<vector<char>> &schematic) {
    if (i < 0 || j < 0 || i > n - 1 || j > m - 1) return false;
    return isdigit(schematic[i][j]);
}

// Given any position of a partNumber, get the full number
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

const vector<vector<int>> dirs = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
const vector<int> dirs1 = {-1, 0, 1};

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
                for (auto &dir : dirs) {
                    if (isPartFunc(i + dir[0], j + dir[1], schematic)) isPart = true;
                }
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
                // Check all combinations of part number above possible gear
                if (isGearFunc(i - 1, j - 1, rows, cols, schematic) && isGearFunc(i - 1, j, rows, cols, schematic) &&
                    isGearFunc(i - 1, j + 1, rows, cols, schematic)) {
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
                    for (auto &dir : dirs1) {
                        if (isGearFunc(i - 1, j + dir, rows, cols, schematic)) {
                            partCount++;
                            string num = getNumber(i - 1, j + dir, cols, schematic);
                            if (!num.empty()) numbers.pb(num);
                        }
                    }
                }

                // Check to the left and right
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

                // Check all possible combinations of parts below gear
                if (isGearFunc(i + 1, j - 1, rows, cols, schematic) && isGearFunc(i + 1, j, rows, cols, schematic) &&
                    isGearFunc(i + 1, j + 1, rows, cols, schematic)) {
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
                    for (auto &dir : dirs1) {
                        if (isGearFunc(i + 1, j + dir, rows, cols, schematic)) {
                            partCount++;
                            string num = getNumber(i + 1, j + dir, cols, schematic);
                            if (!num.empty()) numbers.pb(num);
                        }
                    }
                }

                if (partCount == 2) ratio += stoull(numbers[0]) * stoull(numbers[1]);
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