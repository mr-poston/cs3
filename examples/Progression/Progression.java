/** Generates a simple progression. By default: 0, 1, 2, ... */
public class Progression {
    // Instance variable
    protected long current;

    /** Constructs a progression starting at zero */
    public Progression() {
        this(0);
    }

    /** Constructs a progression with a given start value */
    public Progression(long start) {
        current = start;
    }

    /** Returns the next value of the progression */
    public long nextValue() {
        long answer = current;
        advance();          // this protected call is responsible for advancing the current value
        return answer;
    }

    /** Advances the current value to the next value of the progression */
    protected void advance() {
        current++;
    }

    /** Prints the next n values of the progression, separated by spaces */
    public void printProgression(int n) {
        System.out.print(nextValue());              // print first value without leading space
        for (int i = 1; i < n; i++)
            System.out.print(" " + nextValue());    // print leading space before others
        System.out.println();                       // end the line
    }
}