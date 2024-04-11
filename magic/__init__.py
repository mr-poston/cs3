import check50

@check50.check()
def exists():
    """magic.cpp exists"""
    check50.exists("magic.cpp")

@check50.check()
def util_exists():
    """util.cpp and util.h exist"""
    check50.exists("util.cpp")
    check50.exists("util.h")

@check50.check(exists)
def compiles():
    """Code compiles"""
    check50.run("make magic").exit(0)

@check50.check()
def test1():
    pass