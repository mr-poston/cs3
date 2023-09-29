import java.util.ArrayList;

public class Arguments
{
    ArrayList<String> strList;
    ArrayList<Integer> intList;

    public Arguments(String[] line)
    {
        strList = new ArrayList<>();
        intList = new ArrayList<>();
        for (String s : line)
        {
            try
            {
                intList.add(Integer.parseInt(s));
            }
            catch (Exception e)
            {
                strList.add(s);
            }
        }
    }

    public Arguments(String line)
    {
        strList = new ArrayList<>();
        intList = new ArrayList<>();
        for (String s : line.split(" "))
        {
            strList.add(s);
            try
            {
                intList.add(Integer.parseInt(s));
            }
            catch (Exception e){}
        }
    }

    @Override
    public String toString()
    {
        return strList.toString() + "\n" + intList.toString();
    }
    
    public static void main(String[] args)
    {
        Arguments test = new Arguments(args);
        System.out.println(test);
        System.out.println();
        String line = "";
        for (String s : args)
        {
            line += s + " ";
        }
        test = new Arguments(line);
        System.out.println(test);
    }
}