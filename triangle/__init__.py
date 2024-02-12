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
        desired += " " * (4 - i + 1) + "o" * (2 * i + 1) + "\n"
    desired = desired[:-1]
    check50.run("./trianlge").stdin("4", prompt=True).stdout(desired).exit(0)