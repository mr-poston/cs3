import check50

@check50.check()
def exists():
    """favorites.cpp exists"""
    check50.exists("favorites.cpp")

@check50.check()
def compiles():
    """favorites.cpp compiles"""
    check50.run("make favorites").exit(0);

@check50.check()
def input():
    """Asks for three pieces of information."""
    check50.run("./favorites").stdin("one", prompt=True).stdin("two", prompt=True).stdin("three", prompt=True).stdout("one\ntwo\nthree").exit(0)

# @check50.check()
# def input():
#     """Asks for three pieces of information."""
#     check50.run("./favorites").stdin("one", prompt=True).stdout("one").exit(0)