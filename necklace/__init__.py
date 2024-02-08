import check50

@check50.check()
def exists():
    """necklace.cpp exists"""
    check50.exists("necklace.cpp")

@check50.check(exists)
def compiles():
    """necklace.cpp compiles"""
    check50.run("make necklace").exit(0)

@check50.check(compiles)
def test1():
    """Works for input 3 4"""
    output = check50.run("./necklace").stdin("3 4", prompt=True).stdout()
    if "3 4 7 1 8 9 7 6 3 9 2 1 3 4" not in output:
        raise check50.Failure("Did not display correct necklace: 3 4 7 1 8 9 7 6 3 9 2 1 3 4")
    if "12" not in output:
        raise check50.Failure("Did not count the correct number of steps: 12")

@check50.check(compiles)
def test2():
    """Works for input 3 8"""
    output = check50.run("./necklace").stdin("3 8", prompt=True).stdout()
    if "3 8 11 9 0 9 9 8 7 5 2 7 9 6 5 1 6 7 3 0 3 3 6 9 5 4 9 3 2 5 7 2 9 1 0 1 1 2 3 5 8 3 1 4 5 9 4 3 7 0 7 7 4 1 5 6 1 7 8 5 3 8" not in output:
        raise check50.Failure("Did not display correct necklace: 3 8 11 9 0 9 9 8 7 5 2 7 9 6 5 1 6 7 3 0 3 3 6 9 5 4 9 3 2 5 7 2 9 1 0 1 1 2 3 5 8 3 1 4 5 9 4 3 7 0 7 7 4 1 5 6 1 7 8 5 3 8")
    if "60" not in output:
        raise check50.Failure("Did not count the correct number of steps: 60")

@check50.check(compiles)
def test3():
    """Works for input 2 4"""
    output = check50.run("./necklace").stdin("2 4", prompt=True).stdout()
    if "2 4 6 0 6 6 2 8 0 8 8 6 4 0 4 4 8 2 0 2 2 4" not in output:
        raise check50.Failure("Did not display correct necklace: 2 4 6 0 6 6 2 8 0 8 8 6 4 0 4 4 8 2 0 2 2 4")
    if "20" not in output:
        raise check50.Failure("Did not count the correct number of steps: 20")

@check50.check(compiles)
def test4():
    """Works for secret input"""
    output = check50.run("./necklace").stdin("1 3", prompt=True).stdout()
    if "1 3 4 7 1 8 9 7 6 3 9 2 1 3" not in output:
        raise check50.Failure("Did not display correct necklace")
    if "12" not in output:
        raise check50.Failure("Did not count the correct number of steps")