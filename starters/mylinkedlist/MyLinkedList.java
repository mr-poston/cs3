public class MyLinkedList
{
    // TODO: MyLinkedList instance variables
    

    // TODO: private ListNode class
    

    // TODO: MyLinkedList constructor
    

    //TODO: printFirstToLast method
    

    // TODO: addToEmpty method
    

    // TODO: addToEnd method
    

    // TODO: add method
    

    // TODO: removeFromBeginning method
    

    // TODO: remove method
    

    // TODO: toString method
    

    // main is complete - don't change it
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