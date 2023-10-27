// TODO: Imports
import java.io.File;
import java.io.IOException;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;


public class PQTester
{
    // TODO: Instance variable
    private Queue<String> pq;

    // TODO: Constructors
    public PQTester()
    {
        this("");
    }

    public PQTester(String line)
    {
        setPQ(line);
    }

    // TODO: setPQ method
    public void setPQ(String line)
    {
        pq = new PriorityQueue<>();
        for (String s : line.split(" "))
        {
            pq.offer(s);
        }
    }

    // TODO: getMin method
    public String getMin()
    {
        return pq.peek();
    }

    // TODO: getNaturalOrder method
    public String getNaturalOrder()
    {
        String result = "";
        while(!pq.isEmpty())
        {
            result += pq.poll() + " ";
        }
        return result;
    }

    // TODO: toString mehtod
    @Override
    public String toString()
    {
        return pq.toString();
    }

    // TODO: main method
    public static void main(String[] args)
    {
        PQTester test = new PQTester();
        if (args.length == 0)
        {
            System.out.println(test);
        }
        else if (args[0].equals("pq.dat"))
        {
            try
            {
                Scanner file = new Scanner(new File(args[0]));
                while (file.hasNext())
                {
                    test.setPQ(file.nextLine());
                    System.out.println(test);
                    System.out.println("getMin() - " + test.getMin());
                    System.out.println("getNaturalOrder() - " + test.getNaturalOrder());
                    System.out.println();
                }
            }
            catch (IOException e)
            {
                System.out.println(e);
            }
        }
        else
        {
            test.setPQ(args[0]);
            System.out.println(test);
            System.out.println("getMin() - " + test.getMin());
            System.out.println("getNaturalOrder() - " + test.getNaturalOrder());
        }
    }
}