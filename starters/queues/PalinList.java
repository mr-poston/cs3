// TODO: Imports
import java.io.File;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class PalinList
{
    // TODO: Instance variables
    private Queue<String> q;
    private Stack<String> s;

    // TODO: Constructors
    public PalinList()
    {
        this("");
    }

    public PalinList(String line)
    {
        setList(line);
    }

    // TODO: setList method
    public void setList(String line)
    {
        q = new LinkedList<>();
        s = new Stack<>();
        Scanner scan = new Scanner(line);
        while (scan.hasNext())
        {
            String next = scan.next();
            q.offer(next);
            s.push(next);
        }
    }

    // TODO: isPalin method
    public boolean isPalin()
    {
        while (!q.isEmpty() && !s.isEmpty())
        {
            if (!q.poll().equals(s.pop()))
            {
                return false;
            }
        }
        return true;
    }

    // TODO: toString method
    @Override
    public String toString()
    {
        String result = q.toString() + " is ";
        if (isPalin())
        {
            return result + "a palinlist.";
        }
        return result + "not a palinlist";
    }

    // TODO: main method
    public static void main(String[] args)
    {
        PalinList test = new PalinList();
        if (args.length == 0)
        {
            System.out.println(test);
        }
        else if (args[0].equals("queue.dat"))
        {
            try
            {
                Scanner file = new Scanner(new File(args[0]));
                while (file.hasNext())
                {
                    test.setList(file.nextLine());
                    System.out.println(test);
                }
            }
            catch (IOException e)
            {
                System.out.println(e);
            }
                
        }
        else
        {
            test.setList(args[0]);
            System.out.println(test);
        }
    }
}