import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

public class IteratorRemover {
    // Instance variables
    private ArrayList<String> list;
    private String toRemove;

    // Constructor
    public IteratorRemover(String line, String toRemove) {
        // initialize the instance variables

    }

    // Update methods
    public void setTest(String line, String toRemove) {
        // set new values for the instance variables

    }

    public void remove() {
        // use an Iterator to remove all instances of `toRemove` from `list`

    }

    // toString
    @Override
    public String toString() {
        // return the list in String format
        
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