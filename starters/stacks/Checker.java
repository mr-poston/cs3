/****************************************
 * DO NOT DELETE OR CHANGE THIS FILE!!! *
 ****************************************/
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Checker {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Oops! You should try: java StackTest");
            return;
        }
        int start = 0;
        if (args[0].equals("pop")) {
            start = 1;
        }
        if (args[0].equals("empty")) {
            StackTest test = new StackTest();
            System.out.println(test);
            return;
        }
        String line = "";
        for (int i = start; i < args.length; i++)
        {
            line += args[i] + " ";
        }
        StackTest test = new StackTest(line);
        if (start == 0) {
            System.out.println(test);
        }
        else {
            test.popEmAll();
        }        
    }
}
