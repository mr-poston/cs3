/****************************************
 * DO NOT DELETE OR CHANGE THIS FILE!!! *
 ****************************************/
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Tester {
    public static void main(String[] args) {
        OddEvenSets test;
        if (args[0].equals("filetest")) {
            try {
                Scanner file = new Scanner(new File(args[1]));
            }
            catch (IOException e) {}
        } else {
            test = new OddEvenSets(args[0]);
            System.out.println(test);
        }
    }
}