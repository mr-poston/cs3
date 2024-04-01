#include <iostream>
#include "upper.h"

using namespace std;

/*
 * The main function is complete.
 * You do not need to modify this file!
 */

 int main()
 {
    cout << "Enter a phrase: ";
    string phrase;
    getline(cin, phrase);

    cout << "Converted to Uppercase: " << upperCase(phrase) << endl;

    return 0;
 }