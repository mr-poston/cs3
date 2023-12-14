#include <iostream>

using namespace std;
int main()
{
    // Enter your code here
    cout << "Enter your first string: ";
    string first;
    //cin >> first;
    getline(cin, first);
    cout << "Enter your second string: ";
    string second;
    //cin >> second;
    getline(cin, second);
    
    int middle = second.length() / 2;
    
    second.insert(middle, first);
    
    cout << second << endl;
    
    return 0;
}