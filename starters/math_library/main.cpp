#include <iostream>
#include "math.h"

using namespace std;

/* This code is a tester script and is already
 * completed. You should be able to run once
 * you have completed the math.h and math.cpp
 * files.
 */
int main()
{
    cout << "Please enter two numbers seperated by a space: ";
    int x, y;
    cin >> x >> y;
    
    cout << "Add: " << add(x, y) << endl;
    cout << "Subtract: " << subtract(x, y) << endl;
    cout << "Multiply: " << multiply(x, y) << endl;
    cout << "Divide: " << divide(x, y) << endl;
    
    return 0;
}