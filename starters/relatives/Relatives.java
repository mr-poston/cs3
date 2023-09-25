// Import statements


public class Relatives 
{
    // Instance variable
    

    // Constructor
    

    public void setPersonRelative(String line)
    {
        
    }

    public String getRelatives(String person)
    {
        return "";
    }

    @Override
    public String toString()
    {
        String result = "";
        for (String person : map.keySet())
        {
            result += person + " is related to ";
            for (String s : map.get(person))
            {
                result += s + " ";
            }
            result += "\n";
        }
        return result;
    }

    public static void main(String[] args)
    {
        
    }
}