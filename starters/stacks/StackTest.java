import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;

public class StackTest
{
    // Instance Variable TODO


    // Constructors TODO


    // setStack Method TODO


    // popEmAll Method TODO
    
    
    // toString Method TODO
        

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