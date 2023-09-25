/****************************************
 * DO NOT DELETE OR CHANGE THIS FILE!!! *
 ****************************************/
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Checker {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Oops! You should try: java Acronyms");
            return;
        }
        if (args.length != 1) {
            System.out.println("Invalid args. Try: java Acronyms");
            return;
        }
        Acronyms test = new Acronyms();
        if (args[0].equals("Constructor")) {
            System.out.println(test);
        }
        if (args[0].equals("putEntry")) {
            test.putEntry("RHS - Richardson High School");
            System.out.println(test);
        }
        if (args[0].equals("convert1")) {
            test.putEntry("RHS - Richardson High School");
            String line = "I go to RHS.";
            System.out.println(test.convert(line));
        }
        if (args[0].equals("convert2")) {
            test.putEntry("RHS - Richardson High School");
            String line = "RHS is cool.";
            System.out.println(test.convert(line));
        }
    }
}
