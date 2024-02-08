import check50

@check50.check()
def exists():
    """hacker.cpp exists"""
    check50.exists("hacker.cpp")

@check50.check(exists)
def compiles():
    """hacker.cpp compiles"""
    check50.run("make hacker").exit(0)

@check50.check(compiles)
def test1():
    """Works for input HACK Comp Sci"""
    check50.run("./hacker").stdin("HACK Comp Sci", prompt=True).stdout(".*H4CK C0mp Sc1.*", regex=True).exit(0)

@check50.check(compiles)
def test2():
    """Works for secret input #1"""
    output = check50.run("./hacker").stdin("abcdefghijklmnopqrstuvwxyz", prompt=True).stdout()
    if "4bcd3fgh1jklmn0pqrstuvwxyz" not in output:
        raise check50.Failure("Secret output is incorrect")

@check50.check(compiles)
def test3():
    """Works for secret input #2"""
    output = check50.run("./hacker").stdin("ABCDEFGHIJKLMNOPQRSTUVWXYZ", prompt=True).stdout()
    if "4BCD3FGH1JKLMN0PQRSTUVWXYZ" not in output:
        raise check50.Failure("Secret output is incorrect")