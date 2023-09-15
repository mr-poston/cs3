/****************************************
 * DO NOT DELETE OR CHANGE THIS FILE!!! *
 ****************************************/
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Tester {
    public static void main(String[] args) {
        MathSet test = new MathSet();
        if (args[0].equals("filetest")) {
            try {
                Scanner in = new Scanner(new File("mathsetdata.dat"));
                test = new MathSet(in.nextLine(), in.nextLine());
                System.out.println(test);
            }
            catch (IOException e) {}
        }
        else if (args.length == 3) {
            test = new MathSet(args[1], args[2]);
        }

        if (args[0].equals("union")) {
            System.out.println(test.union());
        }
        else if (args[0].equals("intersection")) {
            System.out.println(test.intersection());
        }
        else if (args[0].equals("differenceAMinusB")) {
            System.out.println(test.differenceAMinusB());
        }
        else if (args[0].equals("differenceBMinusA")) {
            System.out.println(test.differenceAMinusB());
        }
        else if (args[0].equals("symmetricDifference")) {
            System.out.println(test.symmetricDifference());
        }
    }
}
