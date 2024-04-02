import check50

def get_file_lines(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content.split("\n")

@check50.check()
def exists():
    """number.cpp exists"""
    check50.exists("number.cpp")

@check50.check()
def util_exists():
    """util.cpp and util.h exist"""
    check50.exists("util.cpp")
    check50.exists("util.h")

@check50.check(exists)
def compiles():
    """code compiles"""
    check50.run("make number").exit(0)

@check50.check()
def test1():
    """Works for guess too low"""
    check50.run("./number").stdin("50").stdout("Higher!").stdin("84", prompt=False).stdout("Congratulations.*", regex=True).exit(0)

@check50.check()
def test2():
    """Works for guess too high"""
    check50.run("./number").stdin("90").stdout("Lower!").stdin("84", prompt=False).stdout("Congratulations.*", regex=True).exit(0)

@check50.check()
def test3():
    """Uses `randInt` from util library"""
    lines = get_file_lines("number.cpp")
    found = False
    for line in lines:
        if "randInt" in line:
            found = True
    if not found:
        raise check50.Failure("You are required to use randInt from the util library")

@check50.check()
def test4():
    """Uses `readInt` from util library"""
    lines = get_file_lines("number.cpp")
    found = False
    for line in lines:
        if "readInt" in line:
            found = True
    if not found:
        raise check50.Failure("You are required to use readInt from the util library")

@check50.check()
def test5():
    """`setSeed(1);` is not commented out"""
    lines = get_file_lines("number.cpp")
    found = False
    for line in lines:
        if "setSeed(1);" in line:
            found = True
    if not found:
        raise check50.Failure("Make sure `setSeed(1)` is NOT commented out for testing purposes!")