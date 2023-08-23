public abstract class AbstractProgression {
    protected long current;

    public AbstractProgression() {
        this(0);
    }

    public AbstractProgression(long start) {
        current = start;
    }

    public long nextValue() {                   // this is a concrete method
        long answer = current;
        advance();
        return answer;
    }

    public void printProgression(int n) {       // this is a concrete method
        System.out.print(nextValue());
        for (int i = 1; i < n; i++)
            System.out.print(" " + nextValue());
        System.out.println();
    }

    protected abstract void advance();          // notice the lack of a method body
}