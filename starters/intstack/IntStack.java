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
        IntStack test = new IntStack(2);
        test.push(5);
        test.push(7);
        test.push(9);
        System.out.println(test);
        System.out.println(test.isEmpty());
        System.out.println(test.pop());
        System.out.println(test.peek());
        System.out.println(test.pop());
        System.out.println(test.pop());
        try
        {
            System.out.println(test.pop());
        }
        catch (EmptyStackException e)
        {
            System.out.println("OOPS! Stack is empty: can't pop() or peek()");
        }
        System.out.println(test.isEmpty());
        System.out.println(test);
    }
}