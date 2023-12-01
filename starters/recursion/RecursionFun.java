import java.util.Stack;

public class RecursionFun
{
    public static double sumReciprocals(int n)
    {
        // TODO
        return 0.0;
    }

    public static int productOfEvens(int n)
    {
        // TODO
        return 0;
    }

    public static void doubleUp(Stack<Integer> nums)
    {
        // TODO
    }

    public static void countToBy(int n, int m)
    {
        // TODO
    }

    public static int matchingDigits(int a, int b)
    {
        // TODO
        return 0;
    }

    public static void printThis(int n)
    {
        // TODO
    }

    public static void printNums2(int n)
    {
        // TODO
    }

    public static void main(String[] args)
    {
        if (args.length != 1)
        {
            // If you want to add your own tests, do so here

            // Do not change the rest of this method!
            System.out.println("Usage: java RecursionFun methodName");
            return;
        }
        if (args[0].equals("sumReciprocals"))
        {
            System.out.println(sumReciprocals(10));
        }
        if (args[0].equals("productOfEvens"))
        {
            System.out.println(productOfEvens(4));
        }
        if (args[0].equals("doubleUp"))
        {
            Stack<Integer> stack = new Stack<>();
            stack.push(3); stack.push(7); stack.push(12); stack.push(9);
            System.out.println(stack);
            doubleUp(stack);
            System.out.println(stack);
        }
        if (args[0].equals("countToBy"))
        {
            countToBy(34, 5);
            System.out.println();
            countToBy(25, 4);
            System.out.println();
        }
        if (args[0].equals("matchingDigits"))
        {
            System.out.println(matchingDigits(1000, 0));
            System.out.println(matchingDigits(298892, 7892));
        }
        if (args[0].equals("printThis"))
        {
            for (int i = 1; i <= 8; i++)
            {
                printThis(i);
                System.out.println();
            }
        }
        if (args[0].equals("printNums2"))
        {
            for (int i = 1; i <= 10; i++)
            {
                printNums2(i);
                System.out.println();
            }
        }
    }
}
