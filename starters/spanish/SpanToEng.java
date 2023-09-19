import java.io.File;
import java.io.IOException;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class SpanToEng
{
    private Map<String, String> pairs;

    public SpanToEng()
    {
        pairs = new TreeMap<>();
    }

    public void putEntry(String entry)
    {
        String[] words = entry.split(" ");
        pairs.put(words[0], words[1]);
    }

    public String translate(String sentence)
    {
        Scanner scan = new Scanner(sentence);
        String translated = "";
        while (scan.hasNext())
        {
            translated += pairs.get(scan.next()) + " ";
        }
        return translated;
    }

    @Override
    public String toString()
    {
        return pairs.toString().replaceAll(",", "\n");
    }

    public static void main(String[] args)
    {
        try
        {
            Scanner in = new Scanner(new File("spantoeng.dat"));
            SpanToEng test = new SpanToEng();
            int num = in.nextInt();
            in.nextLine();
            for (int i = 0; i < num; i++)
            {
                test.putEntry(in.nextLine());
            }

            System.out.println("==== MAP CONTENTS ====\n");
            System.out.println(test);

            System.out.println("\n==== READ LINES ====\n");
            while (in.hasNext())
            {
                System.out.println(test.translate(in.nextLine()));
            }
        }
        catch (IOException e)
        {
            System.out.println("Cannot read from file.");
        }
    }
}