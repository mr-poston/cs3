import java.io.File;
import java.io.IOException;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

public class Relatives 
{
    // Instance variable
    private Map<String, Set<String>> map;

    // Constructor
    public Relatives()
    {
        map = new TreeMap<>();
    }

    public void setPersonRelative(String line)
    {
        String[] people = line.split(" ");
        if (map.get(people[0]) == null)
        {
            map.put(people[0], new TreeSet<String>());
        }
        map.get(people[0]).add(people[1]);
    }

    public String getRelatives(String person)
    {
        return map.get(person).toString();
    }

    @Override
    public String toString()
    {
        String result = "";
        for (String person : map.keySet())
        {
            result += person + " is related to ";
            for (String s : map.get(person))
            {
                result += s + " ";
            }
            result += "\n";
        }
        return result;
    }

    public static void main(String[] args)
    {
        try
        {
            Scanner scan = new Scanner(new File("relatives.dat"));


            Relatives test = new Relatives();

            int num = scan.nextInt();
            scan.nextLine();
            for (int i = 0; i < num; i++)
            {
                test.setPersonRelative(scan.nextLine());
            }

            System.out.println(test);

            String person = scan.next();
            System.out.println(person + " is related to " + test.getRelatives(person));
        }
        catch (IOException e)
        {
            System.out.println(e);
        }
    }
}