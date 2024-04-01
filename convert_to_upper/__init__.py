import check50

def get_file_lines(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content.split("\n")

@check50.check()
def exists():
    """convert.cpp exists"""
    check50.exists("convert.cpp")

@check50.check()
def exists_h():
    """upper.h exists"""
    check50.exists("upper.h")

@check50.check(exists)
def compiles():
    """convert.cpp compiles"""
    check50.run("make convert").exit(0)

@check50.check(exists_h)
def test1():
    """upperCase function exists in upper.h"""
    lines = get_file_lines("upper.h")
    found = False
    for line in lines:
        if "upperCase" in line:
            found = True
    if not found:
        raise check50.Failure("Make sure to define a function called `upperCase`")

@check50.check(exists_h)
def test2():
    """Correct output for single character"""
    check50.run("./convert").stdin("h").stdout("Converted to Uppercase: H").exit(0)

@check50.check(exists_h)
def test3():
    """Correct output for single word"""
    check50.run("./convert").stdin("hellO").stdout("Converted to Uppercase: HELLO").exit(0)

@check50.check(exists_h)
def test4():
    """Correct output for lowercase phrase"""
    check50.run("./convert").stdin("hello world").stdout("Converted to Uppercase: HELLO WORLD").exit(0)

@check50.check(exists_h)
def test5():
    """Correct output for mixed-case phrase"""
    check50.run("./convert").stdin("hElLo WoRlD").stdout("Converted to Uppercase: HELLO WORLD").exit(0)