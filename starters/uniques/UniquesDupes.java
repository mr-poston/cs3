import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class UniquesDupes {
    public static Set<String> getUniques(String input) {
        // Create a Set of Strings called `uniques` and instantiate it with a TreeSet
        // Create a List of Strings called `list` and instantiate it with an ArrayList using `input`
        // Add items from `list` to `uniques`

        // Return `uniques`
        return null;
    }

    public static Set<String> getDupes(String input) {
        // Create a Set of Strings called `uniques` and instantiate it with a TreeSet
        // Create a Set of Strings called `dupes` and instantiate it with a TreeSet
        // Create a List of Strings called `list` and instantiate it with an ArrayList using `input`
        // Add items from `list` to `uniques` and determine which items should go in `dupes`

        // Return `dupes`
        return null;
    }

    public static void main( String args[] )
	{
		String list = "a b c d e f g h a b c d e f g h i j k"; 
		System.out.println("Original List : " + list);
		System.out.println("Uniques : " + UniquesDupes.getUniques(list));
		System.out.println("Dupes : " + UniquesDupes.getDupes(list) + "\n\n");
		
		list = "one two three one two three six seven one two";
		System.out.println("Original List : " + list);
		System.out.println("Uniques : " + UniquesDupes.getUniques(list));
		System.out.println("Dupes : " + UniquesDupes.getDupes(list) + "\n\n");
		
		list = "1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 6";
		System.out.println("Original List : " + list);
		System.out.println("Uniques : " + UniquesDupes.getUniques(list));
		System.out.println("Dupes : " + UniquesDupes.getDupes(list) + "\n\n");	
	}
}
