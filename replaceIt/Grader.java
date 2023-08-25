public class Grader {
    public static void main(String[] args) {
        IteratorRemover test = new IteratorRemover();
        if (args.length == 2) {
            test.setTest(args[0], args[1]);
            test.remove();
            System.out.println(test);
        }
    }
}