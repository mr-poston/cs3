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
    output = check50.run("java StackTest").stdout()

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
    check50.run("java StackTest empty").stdout("[]", regex=False).exit(0)

def test1():
    """setStack works for input: a 5 _"""
    check50.run("java StackTest a 5 _").stdout("[a, 5, _]", regex=False).exit(0)

def test2():
    """popEmAll works for input: a 5 _"""
    check50.run("java StackTest pop a 5 _").stdout(".*_ 5 a.*", regex=True).exit(0)

def test3():
    """setStack works for input: t a c o c a t"""
    check50.run("java StackTest t a c o c a t").stdout("[t, a, c, o, c, a, t]", regex=False).exit(0)

def test4():
    """popEmAll works for input: t a c o c a t"""
    check50.run("java StackTest pop t a c o c a t").stdout(".*t a c o c a t.*", regex=True).exit(0)

def test5():
    """setStack works for input: works for words too"""
    check50.run("java StackTest works for words too").stdout("[works, for, words, too]", regex=False).exit(0)

def test6():
    """popEmAll works for input: works for words too"""
    check50.run("java StackTest pop works for words too").stdout(".*too words for works.*", regex=True).exit(0)