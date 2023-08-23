public class FibonacciProgression extends Progression {
    protected long previous;

    /** Constructs traditional Fibonacci, starting 0, 1, 1, 2, 3, ... */
    public FibonacciProgression() {
        this(0, 1);
    }

    /** Constructs generalized Fibonacci, with given first and second values */
    public FibonacciProgression(long first, long second) {
        super(first);
        previous = second - first;      // fictitious value preceding the first
    }

    /** Replaces (previous, current) with (current, current+previous) */
    @Override
    protected void advance() {
        long temp = previous;
        previous = current;
        current += temp;
    }
}