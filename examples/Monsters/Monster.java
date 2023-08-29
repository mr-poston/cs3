public class Monster implements Comparable<Monster>{
	private String name;
	protected int age;

	private int myCount;          // each monster gets its own copy of this variable
	private static int count = 0; // all Monsters share this variable

	public Monster() {
		//TODO
	}

	public Monster(String name) {
		// TODO
	}

	public Monster(String name, int age) {
		// TODO
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
		// TODO
	}

	public void setAge(int age) {
		// TODO
	}

	@Override
	public boolean equals(Object obj) {
		// TODO
		return false;
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
		// TODO
		return 0;
	}
}