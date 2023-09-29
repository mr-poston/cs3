import java.util.ArrayList;
import java.util.List;

public class SumArgs
{
    private List<Integer> nums;

    public SumArgs(String line)
    {
        nums = new ArrayList<>();
        for (String s : line.split(" "))
        {
            try
            {
                nums.add(Integer.parseInt(s));
            }
            catch (NumberFormatException e)
            {
                System.out.println(s + " is not an integer!");
            }
        }
    }

    public int findSum()
    {
        int sum = 0;
        for (Integer i : nums)
        {
            sum += i;
        }
        return sum;
    }

    @Override
    public String toString()
    {
        return "" + findSum();
    }

    public static void main(String[] args)
    {
        SumArgs test = new SumArgs(String.join(" ", args));
        System.out.println(test);
    }
}