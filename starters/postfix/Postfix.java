import java.io.File;
import java.io.IOException;
import java.util.EmptyStackException;
import java.util.Scanner;
import java.util.Stack;

public class Postfix
{
    // Instance variables
    private Stack<Double> stack;
    private String expression;

    // Constructors
    public Postfix()
    {
        setExpression("");
    }

    public Postfix(String expression)
    {
        setExpression(expression);
    }

    // setExpression method
    public void setExpression(String expression)
    {
        stack = new Stack<>();
        this.expression = expression;
    }

    // calc method
    public double calc(double one, double two, char op)
    {
        switch(op)
        {
            case '+':
                return one + two;
            case '-':
                return one - two;
            case '*':
                return one * two;
            default:
                return one / two;
        }
    }

    // solve method
    public void solve()
    {
        Scanner scan = new Scanner(expression);
        while (scan.hasNext())
        {
            char value = scan.next().charAt(0);
            if (Character.isDigit(value))
            {
                stack.push(Double.parseDouble("" + value));
                System.out.println(value);
            }
            else
            {
                double two = stack.pop();
                double one = stack.pop();
                System.out.println(">> " + stack.push(calc(one, two, value)));
            }
        }
    }

    @Override
    public String toString()
    {
        try
        {
            return expression + " = " + stack.pop();
        }
        catch (EmptyStackException e)
        {
            return "The expression is empty";
        }
    }

    public static void main(String[] args)
    {
        Postfix test = new Postfix();
        if (args.length == 0)
        {
            test.solve();
            System.out.println(test);
        }
        else if (args[0].equals("postfix.dat"))
        {
            try
            {
                Scanner file = new Scanner(new File("postfix.dat"));
                while (file.hasNext())
                {
                    test.setExpression(file.nextLine());
                    test.solve();
                    System.out.println(test);
                }
            }
            catch (IOException e)
            {
                System.out.println(e);
            }
        }
        else
        {
            String expression = "";
            for (String s : args)
            {
                expression += s + " ";
            }
            test.setExpression(expression.trim());
            test.solve();
            System.out.println(test);
        }
    }
}