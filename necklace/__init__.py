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
