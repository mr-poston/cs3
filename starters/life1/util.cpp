#include "util.h"
#include <iostream>
#include <sstream>
#include <ctime>

using namespace std;

void Error(string message) {
    cerr << "Error: " << message << endl;
    exit(-1);
}

string readLine(const string prompt)
{
    cout << prompt;
    string line;
    getline(cin, line);
    return line;
}

double readDouble(const string prompt, string reprompt) {
    if (reprompt == "") reprompt = prompt;

    double value = 0;
    cout << prompt;
    while (true) {
        string line;
        try {
            if (!getline(cin, line)) {
                throw "getInteger: End of input reached while waiting for integer value.";
            }
        }
        catch (const char *c) {
            cerr << c << endl;
            exit (EXIT_FAILURE);
        }

        istringstream stream(line);
        stream >> value;
        if (!stream.fail() && stream.eof()) {
            break;
        }

        cout<<  reprompt;
    }
    return value;
}

double readDouble(const double low, const double high, const string prompt, string reprompt) {
    if (reprompt == "") reprompt = prompt;
    double value = readDouble(prompt, reprompt);

    while (value < low || value > high) {
        value = readDouble(reprompt);
    }

    return value;
}

int readInt(const string prompt, string reprompt) {
    if (reprompt == "") reprompt = prompt;

    int value = 0;
    cout << prompt;
    while (true) {
        string line;
        try {
            if (!getline(cin, line)) {
                throw "getInteger: End of input reached while waiting for integer value.";
            }
        }
        catch (const char *c) {
            cerr << c << endl;
            exit (EXIT_FAILURE);
        }

        istringstream stream(line);
        stream >> value;
        if (!stream.fail() && stream.eof()) {
            break;
        }

        cout<<  reprompt;
    }
    return value;
}

int readInt(const int low, const int high, const string prompt, string reprompt) {
    if (reprompt == "") reprompt = prompt;
    int value = readInt(prompt, reprompt);

    while (value < low || value > high) {
        value = readInt(reprompt);
    }

    return value;
}

vector<string> splitLine(string input, char delimeter) {

    vector<string> output;
    istringstream stream(input);
    string token;

    while(getline(stream, token, delimeter)) {
        output.push_back(token);
    }
    return output;
}

string toUpperCase(string s) {
    string result;
    for (int i = 0; i < (int)s.length(); i++) {
        result += toupper(s[i]);
    }
    return result;
}

string toLowerCase(string s){
    string result;
    for (int i = 0; i < (int)s.length(); i++) {
        result += tolower(s[i]);
    }
    return result;
}

static void initRandomSeed() {
    static bool initialized = false;
    if (!initialized) {
        srand(int(time(0)));
        rand(); 
        initialized = true;
    }
}

void setSeed(int seed) {
    initRandomSeed();
    srand(seed);
}

int randInt(){
    initRandomSeed();
    return rand();
}

int randInt(int min, int max) {
    initRandomSeed();
    return rand() % (max - min + 1) + min;
}