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
            System.out.println(test);
            // char\t1---5----01---5\n\n
        }
        if (args[0].equals("2")) {
            test = new Histogram("1 2 3 4 5 6 1 2 3 4 5 1 3 1 2 3 4");
            System.out.println(test);
            // char\t1---5----01---5\n1\t\t****\n2\t\t***\n3\t\t****\n4\t\t***\n5\t\t**\n6\t\t*\n
        }
        if (args[0].equals("3")) {
            test = new Histogram();
            test.setSentence("4 T # @ ^ # # #");
            System.out.println(test);
            // char\t1---5----01---5\n\t\t****\n4\t\t*\n@\t\t*\nT\t\t*\n^\t\t*\n
        }
    }
}
