/****************************************
 * DO NOT DELETE OR CHANGE THIS FILE!!! *
 ****************************************/
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Checker {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Oops! You should try: java Relatives");
            return;
        }
        if (args.length != 1) {
            System.out.println("Invalid args. Try: java Relatives");
            return;
        }
        Relatives test = new Relatives();
        if (args[0].equals("Constructor")) {
            System.out.println(test);
        }
        if (args[0].equals("setPersonRelative")) {
            test.setPersonRelative("Almas Brian");
            test.setPersonRelative("Almas Bob");
            test.setPersonRelative("Dot Fred");
            System.out.println(test);
        }
        if (args[0].equals("getRelatives")) {
            test.setPersonRelative("Dot Fred");
            test.setPersonRelative("Dot Tom");
            test.setPersonRelative("Dot Jason");
            test.setPersonRelative("Dot Chuck");
            System.out.println(test.getRelatives("Dot"));
        }
    }
}
