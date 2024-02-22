import check50

@check50.check()
def exists():
    """final_grade.cpp exists"""
    check50.exists("final_grade.cpp")

@check50.check(exists)
def compiles():
    """final_grade.cpp compiles"""
    check50.run("make final_grade").exit(0)

@check50.check(compiles)
def test1():
    """ Works for input 88 73 74 -1"""
    output = check50.run("./final_grade").stdin("88", prompt=True)
                                         .stdin("73", prompt=True)
                                         .stdin("74", prompt=True)
                                         .stdin("-1", prompt=True).stdout()
    for row in output:
        b = " B " in row.upper() and " 85" in row
        c = " C " in row.upper() and " 45" in row
        if not b and not c:
            raise check50.Failure("Output should indicate an average of 85 to get a B and an average of 45 to keep a C")

@check50.check(compiles)
def test2():
    """ Works for input 92 87 -1"""
    output = check50.run("./final_grade").stdin("92", prompt=True)
                                         .stdin("87", prompt=True)
                                         .stdin("-1", prompt=True).stdout()
    for row in output:
        a = " A " in row.upper() and " 90.5" in row
        b = " B " in row.upper() and " 70.5" in row
        if not a and not b:
            raise check50.Failure("Output should indicate an average of 90.5 to get an A and an average of 70.5 to keep a B")

@check50.check(compiles)
def test3():
    """ Works for input 80 80 80 -1"""
    output = check50.run("./final_grade").stdin("80", prompt=True)
                                         .stdin("80", prompt=True)
                                         .stdin("80", prompt=True)
                                         .stdin("-1", prompt=True).stdout()
    for row in output:
        b = " B " in row.upper() and " 80" in row
        a = " A " not in row.upper() and " a " not in row.lower()
        if not b and not a:
            raise check50.Failure("Output should indicate an average of 80 to keep a B but nothing about an A")

@check50.check(compiles)
def test4():
    """ Works for input -1"""
    check50.run("./final_grade").stdin("-1", prompt=True).exit(1)
    