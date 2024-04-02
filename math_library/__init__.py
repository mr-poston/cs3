import check50

def get_file_lines(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content.split("\n")

@check50.check()
def exists1():
    """main.cpp exists"""
    check50.exists("main.cpp")

@check50.check()
def exists2():
    """math.cpp exists"""
    check50.exists("math.cpp")

@check50.check()
def exists3():
    """math.h exists"""
    check50.exists("math.h")

@check50.check()
def compiles():
    """code compiles"""
    check50.run("make math").exit(0)

@check50.check()
def test1():
    """Works for 3 4"""
    check50.run("./math").stdin("3").stdin("4", prompt=False).stdout("Add: 7\nSubtract: -1\nMultiply: 12\nDivide: 0.75").exit(0)

@check50.check()
def test2():
    """Works for 3 0"""
    check50.run("./math").stdin("3").stdin("0", prompt=False).stdout("Add: 3\nSubtract: 3\nMultiply: 0\nDivide: 0").exit(0)

@check50.check()
def test3():
    """Works for 8 2"""
    check50.run("./math").stdin("8").stdin("2", prompt=False).stdout("Add: 10\nSubtract: 6\nMultiply: 16\nDivide: 4").exit(0)