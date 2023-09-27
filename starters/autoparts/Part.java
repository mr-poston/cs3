public class Part implements Comparable<Part>
{
    private String make;
    private String model;
    private String leftOver;
    private int year;

    public Part(String line)
    {
        String[] partPieces = line.split(" ");
        int end = partPieces.length;
        leftOver = "";
        for (int i = 0; i < partPieces.length - 3; i++)
        {
            leftOver += " " + partPieces[i];
        }
        make = partPieces[end - 3];
        model = partPieces[end - 2];
        year = Integer.parseInt(partPieces[end - 1]);
    }

    @Override
    public int compareTo(Part other)
    {
        if (make.equals(other.make))
        {
            if (model.equals(other.model))
            {
                if (year == other.year)
                {
                    return leftOver.compareTo(other.leftOver);
                }
                else if (year > other.year)
                {
                    return 1;
                }
                return -1;
            }
            return model.compareTo(other.model);
        }
        return make.compareTo(other.make);
    }

    @Override
    public String toString()
    {
        return make + " " + model + " " + year + leftOver;
    }
}