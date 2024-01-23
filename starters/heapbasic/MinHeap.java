import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class MinHeap<T extends Comparable<T>>
{
    private List<T> heap;

    public MinHeap()
    {
        // TODO
    }

    @SafeVarargs
    public MinHeap(T... values)
    {
        // TODO
    }

    public T getMin()
    {
        // TODO
    }

    public void add(T value)
    {
        // TODO
    }

    private void swapDown()
    {
        // TODO
    }

    public void remove()
    {
        // TODO
    }

    private void swapUp()
    {
        // TODO
    }

    @Override
    public String toString()
    {
        return heap.toString();
    }

    public void prettyPrint()
    {
        System.out.println("\n\nPRINTING THE HEAP!\n\n");
        int x = 0;
        for(int i = 1; i < heap.size(); i *= 2)
        {
            for(int s = 1; s < heap.size() - i; s++)
            {
                System.out.print(" ");
            }
            for(int j = 0 ; j <= i - 1 && x < heap.size(); j++)
            {
                System.out.print(heap.get(x++) + "  ");
            }
            System.out.println();
            if(x == heap.size() - 1)
            {
                System.out.print(heap.get(x++) + "  ");
            }
        }
        System.out.println();
	}

    public static void main(String[] args)
    {
        MinHeap<Integer> test = null;
        if (args.length == 0)
        {
            System.out.println("No command line arguments given.");
            test = new MinHeap<>(1, 2, 8, 9, 10, 7, 75, 17, 5);
            test.prettyPrint();
        }
        else if (args[0].equals("0"))
        {
            test = new MinHeap<>();
            System.out.println(test);
        }
        else if (args[0].equals("1"))
        {
            test = new MinHeap<>();
            test.add(5);
            System.out.println(test);
        }
        else if (args[0].equals("2"))
        {
            test = new MinHeap<>();
            test.add(3);
            test.add(5);
            System.out.println(test);
        }
        else if (args[0].equals("3"))
        {
            test = new MinHeap<>(5, 10, 1, 6);
            System.out.println(test);
        }
        else if (args[0].equals("4"))
        {
            test = new MinHeap<>(1, 2, 8, 9, 10, 7, 75, 17, 5);
            test.remove()
            test.print()
        }
        else if (args[0].equals("5"))
        {
            test = new MinHeap<>(1, 2, 8, 9, 10, 7, 75, 17, 5);
            test.prettyPrint();
            test.remove();
            test.prettyPrint();
            test.remove();
            test.prettyPrint();
            test.remove();
            test.prettyPrint();
            test.remove();
            test.prettyPrint();
            test.remove();
            test.prettyPrint();
            test.remove();
            test.prettyPrint();
            test.remove();

            test.prettyPrint();
            test.add(25);
            test.prettyPrint();
            test.add(35);
            test.prettyPrint();
            test.remove();
            test.prettyPrint();
            
        }
    }
}
