/****************************************
 * DO NOT DELETE OR CHANGE THIS FILE!!! *
 ****************************************/
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Checker {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Oops! You should try: java SpanToEng");
            return;
        }
        if (args.length != 1) {
            System.out.println("Invalid args");
            return;
        }
        SpanToEng test = new SpanToEng();
        test.putEntry("ordenador computer");
        test.putEntry("quiero want");
        test.putEntry("una a");
        test.putEntry("virus virus");
        test.putEntry("yo i");
        if (args[0].equals("1")) {
            System.out.println(test);
            // {ordenador=computer\n quiero=want\n una=a\n virus=virus\n yo=i}
        }
        if (args[0].equals("2")) {
            System.out.println(test.translate("yo quiero una ordenador virus"));
            // i want a computer virus
        }
    }
}
