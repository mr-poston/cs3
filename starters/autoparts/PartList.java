import java.io.File;
import java.io.IOException;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class PartList
{
    // Instance Variable TODO

    // Constructore
    public PartList()
    {
        // TODO
    }

    public PartList(String filename)
    {
        // TODO
    }

    public void putEntry(Part part)
    {
        // TODO
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