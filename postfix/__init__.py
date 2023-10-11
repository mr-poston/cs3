import check50

@check50.check()
def exists():
    """Postfix.java exists"""
    check50.exists("Postfix.java")

@check50.check()
def compiles():
    """Postfix.java compiles"""
    check50.run("javac Postfix.java").exit(0)

@check50.check()
def file_check():
    """Reads from postfix.dat correctly"""
    output = check50.run("java Postfix postfix.dat").stdout()
    lines = ["2 7 + 1 2 + + = 12.0",
             "1 2 3 4 + + + = 10.0",
             "9 3 * 8 / 4 + = 7.375",
             "3 3 + 7 * 9 2 / + = 46.5",
             "9 3 / 2 * 7 9 * + 4 - = 65.0",
             "5 5 + 2 * 4 / 9 + = 14.0"]
    for line in enumerate(lines):
        if line[1] not in output:
            raise check50.Failure(output + "Should match Sample Output from assignment page")

@check50.check()
def test0():
    """No-parameter constructor / toString works"""
    check50.run("java Postfix").stdout(".*[Ee]mpty.*\n", regex=True).exit(0)

@check50.check()
def test1():
    """Works for input: "4 5 + 7 2 - *" """
    output = check50.run("java Postfix \"4 5 + 7 2 - *\"").stdout()
    if "45.0" not in output:
        raise check50.Failure("Should be \"4 5 + 7 2 - * = 45.0\"; not " + str(output))

@check50.check()
def test2():
    """Works for input: "4 2 3 5 1 - + * +" """
    output = check50.run("java Postfix \"4 2 3 5 1 - + * +\"").stdout()
    if "18.0" not in output:
        raise check50.Failure("Should be \"4 2 3 5 1 - + * + = 18.0\"; not " + str(output))

@check50.check()
def test3():
    """Works for input: "9 3 * 8 / 4 +" """
    output = check50.run("java Postfix \"9 3 * 8 / 4 +\"").stdout()
    if "7.375" not in output:
        raise check50.Failure("Should be \"9 3 * 8 / 4 + = 7.375\"; not " + str(output))

@check50.check()
def test4():
    """Works for input: "3 2 /" """
    output = check50.run("java Postfix \"3 2 /\"").stdout()
    if "1.5" not in output:
        raise check50.Failure("Should be \"3 2 / = 1.5\"; not " + str(output))