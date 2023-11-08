public class IntQueue
{
    // TODO: instance variables
    

    // TODO: constructors
    

    // TODO: offer
    

    // TODO: poll


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
        IntQueue test;
        if (args.length == 0)
        {
            test = new IntQueue();
            test.offer(5);
            test.offer(7);
            test.offer(9);
            test.offer(15);
            System.out.println(test.size());
        }
        else if (args.length == 1)
        {
            test = new IntQueue();
            System.out.println(test.isEmpty());
        }
        else if (args.length == 3)
        {
            test = new IntQueue();
            test.offer(Integer.parseInt(args[0]));
            test.offer(Integer.parseInt(args[1]));
            test.offer(Integer.parseInt(args[2]));
            System.out.println(test);
        }
        else if (args.length == 4)
        {
            test = new IntQueue();
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