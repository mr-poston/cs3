#include "util.h"

int BOARD_SIZE = 15;

// TODO: Write a function that will populate the board with a given number of 'X' chars placed randomly


// TODO: Write a function that will print the board

int main()
{
    // TODO: Create a BOARD_SIZE x BOARD_SIZE grid of 'O' chars


    // Prompt the user for number of active starting cells
    string prompt = "Please enter number of active cells between 1 and "
                    + to_string(BOARD_SIZE * BOARD_SIZE) + ": ";
    int num = readInt(1, BOARD_SIZE * BOARD_SIZE, prompt);

    // TODO: Populate the board


    // TODO: Print the board


    return 0;
}