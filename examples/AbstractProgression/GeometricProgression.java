public class GeometricProgression extends AbstractProgression {
    protected long base;

    /** Constructs progression 1, 2, 4, 8, 16, ... */
    public GeometricProgression() {                     // start at 1 with base of 2
        this(2, 1);
    }

    /** Constructs prigression 1, b, b^2, b^3, b^4, ... */
    public GeometricProgression(long base) {               // start at 1
        this(base, 1);
    }

    /** Constructs geometric progression with arbitrary base and start */
    public GeometricProgression(long base, long start) {
        super(start);
        this.base = base;
    }

    /** Multiplies the current value by the geometric base */
    @Override
    protected void advance() {
        current *= base;                // multiply current by the geometric base
    }
}