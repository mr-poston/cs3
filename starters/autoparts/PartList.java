import java.io.File;
import java.io.IOException;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class PartList
{
    private Map<Part, Integer> partsMap;

    public PartList()
    {
        partsMap = new TreeMap<>();
    }

    public PartList(String filename)
    {
        this();
        try
        {
            Scanner file = new Scanner(new File(filename));
            while(file.hasNext())
            {
                Part part = new Part(file.nextLine());
                putEntry(part);
            }
        }
        catch (IOException e)
        {
            System.out.println(e);
        }
    }

    public void putEntry(Part part)
    {
        if (partsMap.get(part) == null)
        {
            partsMap.put(part, 0);
        }
        partsMap.put(part, partsMap.get(part) + 1);
    }

    @Override
    public String toString()
    {
        String output = "";
        for (Part part : partsMap.keySet())
        {
            output += part + " - " + partsMap.get(part) + "\n";
        }
        return output;
    }

    public static void main(String[] args)
    {
        PartList test = new PartList("autoparts.dat");
        System.out.println(test);
    }
}