import java.util.Collection;

public class BSTBasic<T extends Comparable<T>>
{
    // Instance Variable
    private Node root;

    // Node Class
    private class Node
    {
        // TODO

        public Node(T value, Node left, Node right)
        {
            // TODO
        }
    }

    // Constructors
    public BSTBasic()
    {
        // TODO
    }

    public BSTBasic(Collection<T> values)
    {
        // TODO
    }

    @SafeVarargs
    public BSTBasic(T... values)
    {
        // TODO
    }

    // Adding
    public void add(T value)
    {
        // TODO
    }

    // Searching
    public boolean contains(T item)
    {
        // TODO
        return false;
    }

    // Return the root value
    public T getRoot()
    {
        // TODO
        return null;
    }

    // Traversal Methods
    public void inOrder()
    {
        // TODO
    }

    public void preOrder()
    {
        // TODO
    }

    public void postOrder()
    {
        // TODO
    }

    public void reverseOrder()
    {
        // TODO
    }

    @Override
    public String toString()
    {
        return toString(root);
    }

    private String toString(Node tree)
    {
        if (tree == null)
        {
            return "";
        }
        return toString(tree.left) + " " + tree.value + " " + toString(tree.right);
    }

    /*
     * main
     */
    public static void main(String[] args)
    {
        BSTBasic<Integer> test = new BSTBasic<>(10, 6, 14, 3, 8, 12, 16);
        System.out.println(test.contains(3));
        System.out.println(test.contains(4));
        System.out.println("Root -> " + test.getRoot());
        System.out.print("In Order -> ");
        test.inOrder();
        System.out.print("Pre Order -> ");
        test.preOrder();
        System.out.print("Post Order -> ");
        test.postOrder();
        System.out.print("Reverse Order -> ");
        test.reverseOrder();
        System.out.println("As a string -> " + test);
    }
}
