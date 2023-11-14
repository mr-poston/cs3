public class MyLinkedList
{
    private ListNode head;
    private int size;

    private class ListNode
    {
        int value;
        ListNode next;

        public ListNode(int value, ListNode next)
        {
            this.value = value;
            this.next = next;
        }
    }

    public MyLinkedList()
    {
        head = null;
        size = 0;
    }

    public void printFirstToLast()
    {
        ListNode current = head;
        while (current != null)
        {
            System.out.print(current.value + " ");
            current = current.next;
        }
        System.out.println();
    }

    public void addToEmpty(int value)
    {
        head = new ListNode(value, null);
        size++;
    }

    public void addToEnd(int value)
    {
        ListNode current = head;
        while (current.next != null)
        {
            current = current.next;
        }
        current.next = new ListNode(value, null);
        size++;
    }

    public void add(int index, int value)
    {
        if (index == 0)
        {
            addToEmpty(value);
        }
        else if (index == size)
        {
            addToEnd(value);
        }
        else if (index < size)
        {
            int counter = 1;
            ListNode current = head;
            while (current.next != null)
            {
                if (counter == index)
                {
                    ListNode toInsert = new ListNode(value, current.next);
                    current.next = toInsert;
                    size++;
                    return;
                }
                counter++;
                current = current.next;
            }
        }
        else 
        {
            throw new IndexOutOfBoundsException();
        }
    }

    public int removeFromBeginning()
    {
        int toRemove = head.value;
        head = head.next;
        size--;
        return toRemove;
    }

    public int remove(int index)
    {
        if (index == 0)
        {
            return removeFromBeginning();
        }
        else if (index < size)
        {
            int counter = 1;
            ListNode current = head;
            while (current.next != null)
            {
                if (counter == index)
                {
                    int toRemove = current.next.value;
                    current.next = current.next.next;
                    size--;
                    return toRemove;
                }
                counter++;
                current = current.next;
            }
        }
        else 
        {
            throw new IndexOutOfBoundsException();
        }
        return 0;
    }

    @Override
    public String toString()
    {
        String result = "[";
        ListNode current = head;
        while (current != null)
        {
            result += current.value;
            if (current.next != null)
            {
                result += ", ";
            }
            current = current.next;
        }
        result += "]";
        return result;
    }

    public static void main(String[] args)
    {
        MyLinkedList test = new MyLinkedList();
        if (args.length < 1)
        {
            System.out.println("Must include command line argument!");
        }
        else if (args[0].equals("toString"))
        {
            System.out.println(test);
        }
        else if (args[0].equals("addToEmpty"))
        {
            test.addToEmpty(2);
            System.out.println(test);
        }
        else if (args[0].equals("addToEnd"))
        {
            test.addToEmpty(2);
            test.addToEnd(75);
            System.out.println(test);
        }
        else if (args[0].equals("add"))
        {
            test.addToEmpty(2);
            test.addToEnd(75);
            test.add(1, 21);
            test.add(2, 19);
            System.out.println(test);
        }
        else if (args[0].equals("addOutOfBounds"))
        {
            test.addToEmpty(2);
            try
            {
                test.add(2, 19);
            }
            catch (IndexOutOfBoundsException e)
            {
                System.out.println("Out of Bounds");
            }
        }
        else if (args[0].equals("print"))
        {
            test.addToEmpty(2);
            test.addToEnd(75);
            test.add(1, 21);
            test.add(2, 19);
            test.printFirstToLast();
        }
        else if (args[0].equals("removeFromBeginning"))
        {
            test.addToEmpty(2);
            test.addToEnd(75);
            test.add(1, 21);
            test.add(2, 19);
            test.removeFromBeginning();
            System.out.println(test);
        }
        else if (args[0].equals("remove"))
        {
            test.addToEmpty(2);
            test.addToEnd(75);
            test.add(1, 21);
            test.add(2, 19);
            test.remove(2);
            System.out.println(test);
        }
        else if (args[0].equals("removeOutOfBounds"))
        {
            test.addToEmpty(2);
            try
            {
                test.remove(2);
            }
            catch (IndexOutOfBoundsException e)
            {
                System.out.println("Out of Bounds");
            }
        }
    }
}