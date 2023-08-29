package Monsters;
public class Monster implements Comparable<Monster>{
	private String name;
	protected int age;

	private int myCount;          // each monster gets its own copy of this variable
	private static int count = 0; // all Monsters share this variable

	public Monster() {
		this("noname", 0);
	}

	public Monster(String name) {
		this(name, 0);
	}

	public Monster(String name, int age) {
		this.name = name;
		this.age = age;
		count++;
		myCount = count;
	}

	public String getName() {
		return name;
	}

	public int getAge() {
		return age;
	}

	public int getMyCount() {
		return myCount;
	}

	public static int getCount() {
		return count;
	}

	public void setName(String name) {
		this.name = name;
	}

	public void setAge(int age) {
		this.age = age;
	}

	@Override
	public boolean equals(Object obj) {
		Monster other = (Monster)obj;
		return name == other.name && age == other.age;
	}

	@Override
	public String toString() {
		String result = "Monster " + myCount + " of " + count + ":";
		result += "\n\tName: " + name;
		result += "\n\tAge:  " + age;
		return result;
	}

	@Override
	public int compareTo(Monster other) {
		return age - other.age;
	}
}