import check50

@check50.check()
def exists():
    """PQTester.java exists"""
    check50.exists("PQTester.java")

@check50.check()
def compiles():
    """PQTester.java compiles"""
    check50.run("javac PQTester.java").exit(0)

@check50.check()
def default_constructor():
    """The required constructors exist"""
    f = open("PQTester.java", "r")
    content = f.read()
    if "public PQTester()" not in content:
        raise check50.Failure("Missing the default constructor!")
    if "public PQTester(String" not in content:
        raise check50.Failure("Missing the one-parameter constructor!")
    
@check50.check()
def private_instance_variables():
    """The required private instance variable exists"""
    f = open("PQTester.java", "r")
    content = f.read()
    if "private Queue<String>" not in content:
        raise check50.Failure("Missing the Queue of Strings private instance variable!")

@check50.check()
def file_check():
    """Reads from pq.dat correctly"""
    output = check50.run("java PQTester pq.dat").stdout()
    lines = ["[five, four, seven, two, one, three, six]",
             "getMin() - five",
             "getNaturalOrder() - five four one seven six three two",
             "[1, 2, 3, 4, 5, one, two, three, four, five]",
             "getMin() - 1",
             "getNaturalOrder() - 1 2 3 4 5 five four one three two",
             "[a, b, f, c, d, g, m, e, i, j, k, l, h, n, o, p]",
             "getMin() - a",
             "getNaturalOrder() - a b c d e f g h i j k l m n o p"]
    for line in enumerate(lines):
        if line[1] not in output:
            message = line[1] + "\nThe line above is missing from the output\n"
            message += "   There may be more problems when reading from queue.dat - I just quit looking."
            message += "\n" + output
            raise check50.Failure(message)

@check50.check()
def test0():
    """No-parameter constructor / toString works"""
    check50.run("java PQTester").stdout("[]", regex=False).exit(0)

@check50.check()
def test1():
    """Works for input: "ten twenty thirty fourty" """
    check50.run("java PQTester \"ten twenty thirty fourty\"").stdout("[fourty, ten, thirty, twenty]\ngetMin() - fourty\ngetNaturalOrder() - fourty ten thirty twenty", regex=False).exit(0)

@check50.check()
def test2():
    """Works for input: "a b c d e" """
    check50.run("java PQTester \"a b c d e\"").stdout("[a, b, c, d, e]\ngetMin() - a\ngetNaturalOrder() - a b c d e", regex=False).exit(0)

@check50.check()
def test3():
    """Works for input: "cba abc" """
    check50.run("java PQTester \"abc cba\"").stdout("[abc, cba]\ngetMin() - abc\ngetNaturalOrder() - abc cba", regex=False).exit(0)

@check50.check()
def test4():
    """Works for input: "8 6 7 5 3 0 9" """
    check50.run("java PQTester \"8 6 7 5 3 0 9\"").stdout("[0, 5, 3, 8, 6, 7, 9]\ngetMin() - 0\ngetNaturalOrder() - 0 3 5 6 7 8 9", regex=False).exit(0)