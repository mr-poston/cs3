#include "util.h"

int main()
{
    // Enter your code here
    int secretNumber = randInt(1, 100);
    int guess = 0;
    while (guess != secretNumber) {
        guess = readInt(1, 100, "Guess a number between 1 and 100: ", "That is not between 1 and 100");
        if (guess < secretNumber) {
            cout << "Higher" << endl;
        }
        else if (guess > secretNumber) {
            cout << "Lower!" << endl;
        }
    }
    cout << "Congratulations! You guessed the number!" << endl;
    return 0;
}