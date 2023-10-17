import java.util.EmptyStackException;

public class IntStack
{
    // TODO: instance variables
    

    // TODO: constructors
    

    // TODO: push
    

    // TODO: pop


    // TODO: peek


    // TODO: isEmpty


    // TODO: size


    //TODO: doubleCapacity
    

    // TODO: Complete toString
    @Override
    public String toString()
    {
        return "You have to complete the toString method!";
    }

    // main method - Do not change!
    public static void main(String[] args)
    {
        IntStack test;
        if (args.length == 0)
        {
            test = new IntStack();
            test.push(5);
            test.push(7);
            test.push(9);
            test.push(15);
            System.out.println(test.size());
        }
        else if (args.length == 1)
        {
            test = new IntStack();
            System.out.println(test.isEmpty());
        }
        else if (args.length == 3)
        {
            test = new IntStack(2);
            test.push(Integer.parseInt(args[0]));
            test.push(Integer.parseInt(args[1]));
            test.push(Integer.parseInt(args[2]));
            System.out.println(test);

        }
        else if (args.length == 4)
        {
            test = new IntStack();
            test.push(Integer.parseInt(args[0]));
            test.push(Integer.parseInt(args[1]));
            test.push(Integer.parseInt(args[2]));
            if (args[3].equals("pop"))
            {
                System.out.println(test.pop());
                System.out.println(test.pop());
            }
            else if (args[3].equals("peek"))
            {
                System.out.println(test.peek());
                System.out.println(test.pop());
            }
            else if (args[3].equals("empty"))
            {
                System.out.println(test.isEmpty());
            }
            else if (args[3].equals("exception1"))
            {
                try
                {
                    for (int i = 0; i < 4; i++)
                    {
                        test.pop();
                    }
                }
                catch (EmptyStackException e)
                {
                    System.out.println("OOPS! Stack is empty: can't pop()");
                }
            }
            else if (args[3].equals("exception2"))
            {
                while (!test.isEmpty())
                {
                    test.pop();
                }
                try
                {
                    test.peek();
                }
                catch (EmptyStackException e)
                {
                    System.out.println("OOPS! Stack is empty: can't peek()");
                }
            }
        }
        else
        {
            System.out.println("Must have 0, 1, 3, or 4 arguments");
        }
    }
}