import check50

@check50.check()
def exists():
    """PalinList.java exists"""
    check50.exists("PalinList.java")

@check50.check()
def compiles():
    """PalinList.java compiles"""
    check50.run("javac PalinList.java").exit(0)

@check50.check()
def default_constructor():
    """The required constructors exist"""
    f = open("PalinList.java", "r")
    content = f.read()
    if "public PalinList()" not in content:
        raise check50.Failure("Missing the default constructor!")
    if "public PalinList(String" not in content:
        raise check50.Failure("Missing the one-parameter constructor!")
    
@check50.check()
def private_instance_variables():
    """The required private instance variables exist"""
    f = open("PalinList.java", "r")
    content = f.read()
    if "private Queue<String>" not in content:
        raise check50.Failure("Missing the Queue of Strings private instance variable!")
    if "private Stack<String>" not in content:
        raise check50.Failure("Missing the Stack of Strings private instance variable!")

@check50.check()
def file_check():
    """Reads from queue.dat correctly"""
    output = check50.run("java PalinList queue.dat").stdout()
    lines = ["[one, two, three, two, one] is a ",
             "[1, 2, 3, 4, 5, one, two, three, four, five] is not a ",
             "[a, b, c, d, e, f, g, x, y, z, g, f, h] is not a ",
             "[racecar, is, racecar] is a ",
             "[1, 2, 3, a, b, c, c, b, a, 3, 2, 1] is a ",
             "[chicken, is, a, chicken] is not a "]
    for line in enumerate(lines):
        if line[1] not in output:
            message = line[1] + "\nThe line above is missing from the output\n"
            message += "   There may be more problems when reading from queue.dat - I just quit looking."
            raise check50.Failure(message)

@check50.check()
def test0():
    """No-parameter constructor / toString works"""
    check50.run("java PalinList").stdout("\[\] is a [Pp]alin[Ll]ist.*", regex=True).exit(0)

@check50.check()
def test1():
    """Works for input: "a b c b a" """
    check50.run("java PalinList \"a b c b a\"").stdout("\[.*\] is a [Pp]alin[Ll]ist.*", regex=True).exit(0)

@check50.check()
def test2():
    """Works for input: "a b c d e" """
    check50.run("java PalinList \"a b c d e\"").stdout("\[.*\] is not a [Pp]alin[Ll]ist.*", regex=True).exit(0)

@check50.check()
def test3():
    """Works for input: "abc abc" """
    check50.run("java PalinList \"abc abc\"").stdout("\[.*\] is a [Pp]alin[Ll]ist.*", regex=True).exit(0)

@check50.check()
def test4():
    """Works for input: "a b c a b c" """
    check50.run("java PalinList \"a b c a b c\"").stdout("\[.*\] is not a [Pp]alin[Ll]ist.*", regex=True).exit(0)