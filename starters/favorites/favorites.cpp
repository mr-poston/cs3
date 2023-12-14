#include <iostream>

using namespace std;

int main()
{
    // Enter your code here
    cout << "What is your favorite school subject? ";
    string favSubject;
    getline(cin, favSubject);
    cout << "What is your favorite musical artist or band? ";
    string favArtist;
    getline(cin, favArtist);
    cout << "What is your favorite after-school activity? ";
    string favActivity;
    getline(cin, favActivity);
    
    cout << "Favorite subject: " << favSubject << endl;
    cout << "Favorite artist or band: " << favArtist << endl;
    cout << "Favorite after-school activity: " << favActivity << endl;
    
    return 0;
}