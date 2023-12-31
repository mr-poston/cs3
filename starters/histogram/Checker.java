/****************************************
 * DO NOT DELETE OR CHANGE THIS FILE!!! *
 ****************************************/
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Checker {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Oops! You should try: java Histogram");
            return;
        }
        if (args.length != 1) {
            System.out.println("Invalid args");
            return;
        }
        Histogram test;
        if (args[0].equals("1")) {
            test = new Histogram();
            System.out.println(test.size());
        }
        if (args[0].equals("2")) {
            test = new Histogram("1 2 3 4 5 6 1 2 3 4 5 1 3 1 2 3 4");
            System.out.println(test);
        }
        if (args[0].equals("3")) {
            test = new Histogram();
            test.setSentence("4 T # @ ^ # # #");
            System.out.println(test);
        }
    }
}
