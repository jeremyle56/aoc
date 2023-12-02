#include <bits/stdc++.h>
using namespace std;

const string INPUT_FILE_NAME = "input.txt";

// Reads file from input files into a vector
bool readFile(vector<string> &lines) {
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

// Splits a string with a given delimiter to a vector
vector<string> split(string s, string delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    string token;
    vector<string> res;

    while ((pos_end = s.find(delimiter, pos_start)) != string::npos) {
        token = s.substr(pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back(token);
    }

    res.push_back(s.substr(pos_start));
    return res;
}