#ifndef _util
#define _util

#include <iostream>
#include <vector>

using  namespace std;

void Error(string message);

string readLine(const string prompt = "?");

int readInt(const string prompt = "?", string reprompt = "");
int readInt(const int low, const int high, const string prompt = "?", string reprompt = "");

double readDouble(const string prompt = "?", string reprompt = "");
double readDouble(const double low, const double high, const string prompt = "?", string reprompt = "");

vector<string> splitLine(string input, char delimeter = ' ');

string toUpperCase(string s);
string toLowerCase(string s);

void setSeed(int seed);
int randInt();
int randInt(int min, int max);

#endif