import check50

@check50.check()
def exists():
    """buggy.cpp exists"""
    check50.exists("buggy.cpp")

@check50.check(exists)
def compiles():
    """buggy.cpp compiles"""
    check50.run("make buggy").exit(0)

@check50.check(compiles)
def test1():
    """Correct output when using example.txt"""
    check50.run("./buggy").stdin("example.txt").stdout("25").exit(0)

@check50.check(compiles)
def test2():
    """Correct output when using example.txt"""
    check50.run("./buggy").stdin("input.txt").stdout("1489").exit(0)