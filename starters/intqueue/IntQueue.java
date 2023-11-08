import java.util.ArrayList;

public class intQueue
{
    private int[] rayOfInts;
    private int numInts;

    public intQueue()
    {
        this(10);
    }

    public intQueue(int initialCap)
    {
        rayOfInts = new int[initialCap];
        numInts = 0;
    }

    public void offer(int num)
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

    public Integer poll()
    {
        if (numInts == 0)
        {
            return null;
        } 
        int result = rayOfInts[0];
        int[] temp = new int[rayOfInts.length];
        for (int i = 1; i < numInts; i++)
        {
            temp[i - 1] = rayOfInts[i];
        }
        rayOfInts = temp;
        numInts--;
        return result;
    }

    public Integer peek()
    {
        if (numInts == 0)
        {
            return null;
        }
        return rayOfInts[0];
    }

    public boolean isEmpty()
    {
        return numInts == 0;
    }

    public int size()
    {
        return numInts;
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
        intQueue test;
        if (args.length == 0)
        {
            test = new intQueue();
            test.offer(5);
            test.offer(7);
            test.offer(9);
            test.offer(15);
            System.out.println(test.size());
        }
        else if (args.length == 1)
        {
            test = new intQueue();
            System.out.println(test.isEmpty());
        }
        else if (args.length == 3)
        {
            test = new intQueue();
            test.offer(Integer.parseInt(args[0]));
            test.offer(Integer.parseInt(args[1]));
            test.offer(Integer.parseInt(args[2]));
            System.out.println(test);
        }
        else if (args.length == 4)
        {
            test = new intQueue();
            test.offer(Integer.parseInt(args[0]));
            test.offer(Integer.parseInt(args[1]));
            test.offer(Integer.parseInt(args[2]));
            if (args[3].equals("poll"))
            {
                System.out.println(test.poll());
                System.out.println(test.poll());
            }
            else if (args[3].equals("peek"))
            {
                System.out.println(test.peek());
                System.out.println(test.poll());
            }
            else if (args[3].equals("empty"))
            {
                System.out.println(test.isEmpty());
            }
            else if (args[3].equals("badPoll"))
            {
                while (!test.isEmpty())
                {
                    test.poll();
                }
                System.out.println(test.poll());
            }
            else if (args[3].equals("badPeek"))
            {
                while (!test.isEmpty())
                {
                    test.poll();
                }
                System.out.println(test.peek());
            }
        }
        else 
        {
            System.out.println("Must have 0, 1, 3, or 4 command-line arguments");
        }
    }
}