import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;

public class StackTest
{
    // Instance Variable
    private Stack<String> stack;

    // Constructors
    public StackTest()
    {
        this("");
    }

    public StackTest(String line)
    {
        setStack(line);
    }

    public void setStack(String line)
    {
        stack = new Stack<>();
        for (String s : line.split(" "))
        {
            stack.push(s);
        }
    }

    public void popEmAll()
    {
        System.out.println("popping all items from the stack");
        while (!stack.isEmpty())
        {
            System.out.print(stack.pop() + " ");
        }
        System.out.println("\n");
    }

    @Override
    public String toString()
    {
        return stack.toString();
    }

    public static void main(String[] args)
    {
        StackTest test = new StackTest();

        try
        {
            Scanner file;
            if (args.length > 0)
            {
                file = new Scanner(new File(args[0]));
            }
            else
            {
                file = new Scanner(new File("stackdata.dat"));
            }
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

}