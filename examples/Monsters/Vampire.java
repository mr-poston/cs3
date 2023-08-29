public class Vampire extends Monster {
    public Vampire(String name) {
        super(name);
    }

    public Vampire(String name, int age) {
        super(name, age);
    }

    public void showPrivate() {
        System.out.println("showPrivate() - accessing name");
        //System.out.println(name); // name has private access in Monster
    }

    public void showProtected() {
        System.out.println("showProtected() - accessing age");
        age = 90876;
        System.out.println(age);
    }
}