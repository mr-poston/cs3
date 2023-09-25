import java.io.File;
import java.io.IOException;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class Acronyms
{
    // Instance variable
    private Map<String, String> table;

    // Constructor
    public Acronyms()
    {
        table = new TreeMap<>();
    }

    public void putEntry(String entry)
    {
        String[] pair = entry.split(" - ");
        table.put(pair[0], pair[1]);
    }

    public String convert(String line)
    {
        Scanner scan = new Scanner(line);
        String result = "";
        while (scan.hasNext())
        {
            String word = scan.next();
            String noPunct = word.replaceAll("\\.", "");
            if (table.get(noPunct) == null)
            {
                result += word + " ";
            }
            else if (!word.equals(noPunct))
            {
                result += table.get(noPunct) + ". ";
            }
            else
            {
                result += table.get(word) + " ";
            }
        }
        return result;
    }

    @Override
    public String toString()
    {
        return table.toString().replaceAll(",", "\n");
    }

    public static void main(String[] args)
    {
        try
        {
            Scanner file = new Scanner(new File("acronyms.dat"));

            Acronyms test = new Acronyms();

            int num = file.nextInt();
            file.nextLine();
            for (int i = 0; i < num; i++)
            {
                test.putEntry(file.nextLine());
            }

            System.out.println("==== MAP CONTENTS ====\n");
            System.out.println(test);

            System.out.println("\n==== READ LINES ====\n");
            while (file.hasNext())
            {
                String line = test.convert(file.nextLine());
                System.out.println(line);
            }
        }
        catch (IOException e)
        {
            System.out.println(e);
        }
    }
}