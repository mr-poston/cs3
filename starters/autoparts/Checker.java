/****************************************
 * DO NOT DELETE OR CHANGE THIS FILE!!! *
 ****************************************/
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Checker {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Oops! You should try: java PartList");
            return;
        }
        if (args.length != 2) {
            System.out.println("Invalid args. Try: java PartList");
            return;
        }
        if (args[0].equals("part")) {
            Part part1 = new Part("Radiator 74219 Chrystler Pacifica 2019");
            Part part2;
            if (args[1].equals("constructor")) {
                System.out.println(part1);
            }
            else if (args[1].equals("compare1")) {
                part2 = new Part("Radiator 12345 Dodge Ram 2020");
                System.out.println(part1.compareTo(part2));
            }
            else if (args[1].equals("compare2")) {
                part2 = new Part("Wiper Blades 09876 Chrystler 300 2023");
                System.out.println(part1.compareTo(part2));
            }
            else if (args[1].equals("compare3")) {
                part2 = new Part("Fuel Pump 39846 Chrystler Pacifica 2022");
                System.out.println(part1.compareTo(part2));
            }
            else if (args[1].equals("compare4")) {
                part2 = new Part("Fuel Pump 39846 Chrystler Pacifica 2019");
                System.out.println(part1.compareTo(part2));
            }
        }
        else if (args[0].equals("list")) {
            PartList list = new PartList();
            if (args[1].equals("empty")) {
                System.out.println(list);
            }
            else if (args[1].equals("putEntry1")) {
                list.putEntry(new Part("Water Pump 19934 Ford Taurus 1999"));
                System.out.println(list);
            }
            else if (args[1].equals("putEntry2")) {
                list.putEntry(new Part("Water Pump 19934 Ford Taurus 1999"));
                list.putEntry(new Part("Water Pump 19934 Ford Taurus 1999"));
                System.out.println(list);
            }
        }
    }
}
