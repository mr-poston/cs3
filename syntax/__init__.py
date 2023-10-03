import check50

@check50.check()
def exists():
    """SyntaxChecker.java exists"""
    check50.exists("SyntaxChecker.java")

@check50.check()
def compiles():
    """SyntaxChecker.java compiles"""
    check50.run("javac SyntaxChecker.java").exit(0)

@check50.check()
def file_check():
    """Reads from syntax.dat correctly"""
    output = check50.run("java SyntaxChecker syntax.dat").stdout()
    lines = ["(abc(*def) is incorrect",
             "[{}] is correct",
             "[ is incorrect",
             "[{<()>}] is correct",
             "{<html[value=4]*(12)>{$x}} is correct",
             "[one]<two>{three}(four) is correct",
             "car(cdr(a)(b))) is incorrect",
             "car(cdr(a)(b)) is correct"]
    for line in enumerate(lines):
        if line[1] not in output:
            raise check50.Failure(output + "Should match Sample Output from assignment page")

@check50.check()
def test0():
    """No-parameter constructor works"""
    check50.run("java SyntaxChecker").stdout("No expression given.*\n", regex=True).exit(0)

@check50.check()
def test1():
    """Works for input: "[{}]" """
    output = check50.run("java SyntaxChecker [{}]").stdout().split("\n")
    while "" in output:
        output.remove("")
    if "is correct" not in output[0]:
        raise check50.Failure("\"[{}]\" should be correct; not " + str(output[0]))

@check50.check()
def test2():
    """Works for input: "(abc(*def)" """
    output = check50.run("java SyntaxChecker (abc(*def)").stdout().split("\n")
    while "" in output:
        output.remove("")
    if "incorrect" not in output[0]:
        raise check50.Failure("\"(abc(*def)\" should be incorrect; not " + str(output[0]))

@check50.check()
def test3():
    """Works for input: "{(})" """
    output = check50.run("java SyntaxChecker {(})").stdout().split("\n")
    while "" in output:
        output.remove("")
    if "incorrect" not in output[0]:
        raise check50.Failure("\"{(})\" should be incorrect; not " + str(output[0]))

@check50.check()
def test4():
    """Works for input: "<>" """
    output = check50.run("java SyntaxChecker <>").stdout().split("\n")
    while "" in output:
        output.remove("")
    if "is correct" not in output[0]:
        raise check50.Failure("\"<>\" should be correct; not " + str(output[0]))