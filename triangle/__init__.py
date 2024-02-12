import check50

@check50.check()
def exists():
    """triangle.cpp exists"""
    check50.exists("triangle.cpp")

@check50.check(exists)
def compiles():
    """triangle.cpp compiles"""
    check50.run("make triangle").exit(0)

@check50.check(compiles)
def test1():
    """Works for input of 4"""
    desired = ""
    for i in range(4):
        desired += " " * (4 - i - 1) + "o" * (2 * i + 1) + "\n"
    desired = desired[:-1]
    check50.run("./triangle").stdin("4", prompt=True).stdout(desired).exit(0)

@check50.check(compiles)
def test2():
    """Works for input of 6"""
    desired = ""
    for i in range(6):
        desired += " " * (6 - i - 1) + "o" * (2 * i + 1) + "\n"
    desired = desired[:-1]
    check50.run("./triangle").stdin("6", prompt=True).stdout(desired).exit(0)

@check50.check(exists)
def test3():
    """printSpaces function exists"""
    f = open("triangle.cpp", "r")
    contents = f.read()
    found = False
    for line in contents:
        if "printSpaces" in line:
            found = True
            while " " in line:
                line = line.remove(" ")
            if "voidprintSpaces(int" not in line:
                raise check50.Failure("function header should be:\nvoid printSpaces(int num)")
            break
    if not found:
        raise check50.Failure("printSpaces function not found")

@check50.check(exists)
def test4():
    """printCircles function exists"""
    f = open("triangle.cpp", "r")
    contents = f.read()
    found = False
    for line in contents:
        if "printCircles" in line:
            found = True
            while " " in line:
                line = line.remove(" ")
            if "voidprintCircles(int" not in line:
                raise check50.Failure("function header should be:\nvoid printCircles(int num)")
            break
    if not found:
        raise check50.Failure("printCircles function not found")
