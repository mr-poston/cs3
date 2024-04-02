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
    check50.run("make main").exit(0)

@check50.check()
def test1():
    pass