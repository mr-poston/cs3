import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

public class IteratorRemover {
    // Instance variables
    private ArrayList<String> list;
    private String toRemove;

    // Constructor
    public IteratorRemover(String line, String toRemove) {
        setTest(line, toRemove);
    }

    // Update methods
    public void setTest(String line, String toRemove) {
        list = new ArrayList<>(Arrays.asList(line.split(" ")));
        this.toRemove = toRemove;
    }

    public void remove() {
        Iterator<String> it = list.iterator();
        while (it.hasNext()) {
            if (it.next().equals(toRemove)) {
                it.remove();
            }
        }
    }

    // toString
    @Override
    public String toString() {
        return list.toString();
    }

    // main method
    public static void main(String[] args) {
        IteratorRemover test = new IteratorRemover("a b c a b c", "a");
        test.remove();
        System.out.println(test);

        test.setTest("a b c d e f g h i j x x x x", "x");
        test.remove();
        System.out.println(test);

        test.setTest("1 2 3 4 5 6 a b c a b c", "b");
        test.remove();
        System.out.println(test);
    }
}