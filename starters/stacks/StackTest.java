import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;

public class StackTest
{
    // Instance Variable TODO
    private Stack<String> stack;

    // Constructors TODO
    public StackTest()
    {
        this("");
    }

    public StackTest(String line)
    {
        setStack(line);
    }

    // setStack Method TODO
    public void setStack(String line)
    {
        stack = new Stack<>();
        for (String s : line.split(" "))
        {
            stack.push(s);
        }
    }

    // popEmAll Method TODO
    public void popEmAll()
    {
        System.out.println("popping all items from the stack");
        while (!stack.isEmpty())
        {
            System.out.print(stack.pop() + " ");
        }
        System.out.println("\n");
    }
    
    // toString Method TODO
    @Override
    public String toString()
    {
        return stack.toString();
    }
    

    public static void main(String[] args)
    {
        StackTest test = new StackTest();
        if (args.length == 0)
        {
            System.out.println(test);
        }
        else if (args[0].equals("stackdata.dat"))
        {
            try
            {
                Scanner file = new Scanner(new File(args[0]));
                while (file.hasNext())
                {
                    test.setStack(file.nextLine());
                    System.out.println(test);
                    test.popEmAll();
                }
            }
            catch (IOException e)
            {
                System.out.println(e);
            }
        }
        else if (args.length > 0)
        {
            test.setStack(args[0]);
            System.out.println(test);
            test.popEmAll();
        }
    }
}