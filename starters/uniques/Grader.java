/****************************************
 * DO NOT DELETE OR CHANGE THIS FILE!!! *
 ****************************************/
import static java.lang.System.*;

public class Grader {
    public static void main(String[] args) {
        out.println(args[0]);
        out.println(UniquesDupes.getUniques(args[0]));
        out.println(UniquesDupes.getDupes(args[0]));
    }
}
