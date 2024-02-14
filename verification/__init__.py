import check50

@check50.check()
def exists():
    """verification.cpp exists"""
    check50.exists("verification.cpp")

@check50.check(exists)
def compiles():
    """verification.cpp compiles"""
    check50.run("make verification").exit(0)

@check50.check(compiles)
def test1():
    """Correctly computes the number of matches per 100,000 tests"""
    check50.run("./verification").stdin("100000", prompt=True).stdout("30").exit(0)

check50.check(compiles)
def test2():
    """Correctly computes the number of matches per 200,000 tests"""
    check50.run("./verification").stdin("200000", prompt=True).stdout("63").exit(0)