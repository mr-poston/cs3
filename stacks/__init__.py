import check50

@check50.check()
def exists():
    """StackTest.java exists"""
    check50.exists("StackTest.java")

@check50.check()
def compiles():
    """StackTest.java compiles"""
    check50.run("javac StackTest.java").exit(0)

@check50.check()
def file_check():
    """Reads from stackdata.dat correctly"""
    output = check50.run("java StackTest stackdata.dat").stdout()
    lines = ["[a, b, c, d, e, f, g, h, i]",
             "i h g f e d c b a",
             "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
             "10 9 8 7 6 5 4 3 2 1",
             "[#, $, %, ^, *, (, ), ), _]",
             "_ ) ) ( * ^ % $ #"]
    for line in enumerate(lines):
        if line[1] not in output:
            raise check50.Failure(output + "Should match Sample Output from assignment page")

@check50.check()
def test0():
    """No-parameter constructor works"""
    check50.run("java StackTest").stdout("[]", regex=False).exit(0)

def test1():
    """Works for input: "a 5 _" """
    output = check50.run("java StackTest \"a 5 _\"").stdout().split("\n")
    while "" in output:
        output.remove("")
    if "[a, 5, _]" not in output[0]:
        raise check50.Failure("setStack should return \"[a, 5, _]\" for input \"a 5 _\"")
    if "popping all items from the stack" not in output[1]:
        raise check50.Failure("Does popEmAll print \"popping all items from the stack\"?")
    if "_ 5 a" not in output[2]:
        raise check50.Failure("popEmAll should return \"_ 5 a\" for input \"a 5 _\"")
    
def test2():
    """Works for input: "t a c o c a t" """
    output = check50.run("java StackTest \"t a c o c a t\"").stdout().split("\n")
    while "" in output:
        output.remove("")
    if "[t, a, c, o, c, a, t]" not in output[0]:
        raise check50.Failure("setStack should return \"[t, a, c, o, c, a, t]\" for input \"t a c o c a t\"")
    if "popping all items from the stack" not in output[1]:
        raise check50.Failure("Does popEmAll print \"popping all items from the stack\"?")
    if "_ 5 a" not in output[2]:
        raise check50.Failure("popEmAll should return \"t a c o c a t\" for input \"t a c o c a t\"")
    
def test3():
    """Works for input: "works for words too" """
    output = check50.run("java StackTest \"works for words too\"").stdout().split("\n")
    while "" in output:
        output.remove("")
    if "[works, for, words, too]" not in output[0]:
        raise check50.Failure("setStack should return \"[works, for, words, too]\" for input \"works for words too\"")
    if "popping all items from the stack" not in output[1]:
        raise check50.Failure("Does popEmAll print \"popping all items from the stack\"?")
    if "_ 5 a" not in output[2]:
        raise check50.Failure("popEmAll should return \"too words for works\" for input \"works for words too\"")

def test5():
    """Works for input: "works for words too" """
    check50.run("java StackTest works for words too").stdout("[works, for, words, too]", regex=False).exit(0)