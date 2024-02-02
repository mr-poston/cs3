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
    check50.run("./favorites").stdin("one", prompt=True).stdin("two", prompt=True).stdin("three", prompt=True).exit(0)

@check50.check()
def input():
    """Repeats the information from input."""
    check50.run("./favorites").stdin("subject", prompt=True).stdin("music", prompt=True).stdin("hobby", prompt=True).stdout(".*subject\n.*music\n.*hobby", regex=True).exit(0)