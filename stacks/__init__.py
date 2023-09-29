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
            raise check50.Failure(output)

@check50.check()
def test0():
    """StackTest.java constructor works"""
    check50.run("java StackTest test1.dat").stdout("Chrystler Pacifica 2019 Radiator 74219", regex=False).exit(0)
