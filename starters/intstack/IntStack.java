import java.util.EmptyStackException;

public class IntStack
{
    private int[] rayOfInts;
    private int numInts;

    public IntStack()
    {
        this(10);
    }

    public IntStack(int initialCap)
    {
        rayOfInts = new int[initialCap];
        numInts = 0;
    }

    public void push(int num)
    {
        if (numInts == rayOfInts.length)
        {
            doubleCapacity();
        }
        rayOfInts[numInts++] = num;
    }

    private void doubleCapacity()
    {
        int[] temp = new int[rayOfInts.length * 2];
        for (int i = 0; i < rayOfInts.length; i++)
        {
            temp[i] = rayOfInts[i];
        }
        rayOfInts = temp;
    }

    public int pop()
    {
        if (numInts == 0)
        {
            throw new EmptyStackException();
        }
        return rayOfInts[--numInts];
    }

    public boolean isEmpty()
    {
        return numInts == 0;
    }

    public int size()
    {
        return numInts;
    }

    public int peek()
    {
        if (numInts == 0)
        {
            throw new EmptyStackException();
        }
        return rayOfInts[numInts - 1];
    }

    @Override
    public String toString()
    {
        String result = "[";
        for (int i = 0; i < numInts; i++)
        {
            result += rayOfInts[i];
            if (i < numInts - 1)
            {
                result += ", ";
            }
        }
        result += "]";
        return result;
    }

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
            else if (args[3].equals("exception"))
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
                    System.out.println("OOPS! Stack is empty: can't pop() or peek()");
                }
                try
                {
                    test.peek();
                }
                catch (EmptyStackException e)
                {
                    System.out.println("OOPS! Stack is empty: can't pop() or peek()");
                }
            }
        }
        else
        {
            System.out.println("Must have 0, 1, 3, or 4 arguments");
        }
    }
}