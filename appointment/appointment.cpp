#include <iostream>
#include <vector>

using namespace std;

string nextAppointment(string type, int day, int daysToNext = 7);

int main()
{
    // Enter your code here
    cout << "What type of appointment do you have? ";
    string type;
    cin >> type;
    cout << "Which day is your appointment?" << endl;
    cout << "1: Sunday\n2: Monday\n3: Tuesday\n4: Wednesday\n5: Thursday\n";
    cout << "6: Friday\n7: Saturday\n";
    int day;
    cin >> day;
    string next;
    if (type == "Oncologist") {
        next = nextAppointment(type, day, 2);
    } else if (type == "Orthodontist") {
        next = nextAppointment(type, day, 10);
    } else {
        next = nextAppointment(type, day);
    }
    cout << "Your follow up will be on a " << next << endl;
    return 0;
}

string nextAppointment(string type, int day, int daysToNext) {
    vector<string> daysOfWeek {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday"};
    int next = day + daysToNext - 1;
    while (next >= daysOfWeek.size()) {
        next -= 7;
    }
    return daysOfWeek[next];
}
