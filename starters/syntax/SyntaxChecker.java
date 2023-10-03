import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;

public class SyntaxChecker
{
    // Instance variables TODO
    private String expression;
    private Stack<String> symbols;

    // Constructors TODO
    public SyntaxChecker()
    {
        setExpression("");
    }

    public SyntaxChecker(String line)
    {
        setExpression(line);
    }

    // setExpression TODO
    public void setExpression(String line)
    {
        expression = line;
        symbols = new Stack<>();
    }

    // checkExpression TODO
    public boolean checkExpression()
    {
        String open = "{(<[";
        String close = "})>]";
        String[] list = expression.split("");
        for (int i = 0; i < list.length; i++)
        {
            String s = list[i];
            if (open.indexOf(s) > -1)
            {
                symbols.push(s);
            }
            else if (close.indexOf(s) > -1)
            {
                if (symbols.isEmpty())
                {
                    return false;
                }
                String op = symbols.pop();
                if (close.indexOf(s) != open.indexOf(op))
                {
                    return false;
                }
            }
        }
        return symbols.isEmpty();
    }

    // toString TODO
    @Override
    public String toString()
    {
        if (expression.equals(""))
        {
            return "No expression given.\n";
        }
        if (checkExpression())
        {
            return expression + " is correct.\n";
        }
        return expression + " is incorrect.\n";
    }

    // main TODO
    public static void main ( String[] args )
	{
        SyntaxChecker test = new SyntaxChecker();
        if (args.length == 0)
        {
            System.out.println(test);
        }
        else if (args[0].equals("syntax.dat"))
        {
            try
            {
                Scanner file = new Scanner(new File(args[0]));
                while (file.hasNext())
                {
                    test.setExpression(file.nextLine());
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
            test.setExpression(args[0]);
            System.out.println(test);
        }
	}
}