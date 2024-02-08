import check50

@check50.check()
def exists():
    """sum_digits.cpp exists"""
    check50.exists("sum_digits.cpp")

@check50.check(exists)
def compiles():
    """sum_digits.cpp compiles"""
    check50.run("make sum_digits").exit(0)

@check50.check(compiles)
def test1():
    """Works for input 6835"""
    output = check50.run("./sum_digits").stdin("6835", prompt=True).stdout()
    lines = output.split("\n")
    if "22" not in lines[1]:
        raise check50.Failure("Output should show a sum of 22")

@check50.check(compiles)
def test2():
    """Works for input 123"""
    output = check50.run("./sum_digits").stdin("123", prompt=True).stdout()
    lines = output.split("\n")
    if "6" not in lines[1]:
        raise check50.Failure("Output should show a sum of 6")

@check50.check(compiles)
def test3():
    """Works for secret input #1"""
    output = check50.run("./sum_digits").stdin("1975", prompt=True).stdout()
    lines = output.split("\n")
    if "22" not in lines[1]:
        raise check50.Failure("Output shows incorrect sum")

@check50.check(compiles)
def test4():
    """Works for secret input #2"""
    output = check50.run("./sum_digits").stdin("2024", prompt=True).stdout()
    lines = output.split("\n")
    if "8" not in lines[1]:
        raise check50.Failure("Output shows incorrect sum")