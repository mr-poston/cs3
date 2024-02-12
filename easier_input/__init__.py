import check50

@check50.check()
def exists():
    """easier_input.cpp exists"""
    check50.exists("easier_input.cpp")

@check50.check(exists)
def compiles():
    """easier_input.cpp compiles"""
    check50.run("make easier_input").exit(0)

@check50.check(compiles)
def test1():
    """Works when user enters valid input"""
    outcheck = "You entered: hello\n"
    outcheck += "You entered: 3.14"
    outcheck += "You entered: 0.5"
    outcheck += "You entered: 22"
    outcheck += "You entered: 3"
    check50.run("./easier_input").stdin("hello", "3.14", "0.5", "22", "3", prompt=True).stdout(outcheck).exit(0)

def test2():
    """Works when user enters out of range double"""
    outcheck = "You entered: hello\n"
    outcheck += "You entered: 3.14"
    outcheck += "You entered: 0.5"
    outcheck += "You entered: 22"
    outcheck += "You entered: 3"
    check50.run("./easier_input").stdin("hello 3.14 3.4 0.5 22 3", prompt=True).stdout(outcheck).exit(0)

@check50.check(compiles)
def test3():
    """Works when user enters out of range int"""
    outcheck = "You entered: hello\n"
    outcheck += "You entered: 3.14"
    outcheck += "You entered: 0.5"
    outcheck += "You entered: 22"
    outcheck += "You entered: 3"
    check50.run("./easier_input").stdin("hello 3.14 0.5 22 18 3", prompt=True).stdout(outcheck).exit(0)