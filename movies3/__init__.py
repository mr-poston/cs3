import check50

@check50.check()
def exists():
    """movies.cpp exists"""
    check50.exists("movies.cpp")

@check50.check(exists)
def compiles():
    """movies.cpp compiles"""
    check50.run("make movies").exit(0)

@check50.check(exists)
def test0():
    raise check50.Failure("This test failed because the tests are incomplete. Please try again later.")

@check50.check(compiles)
def test1():
    check50.run("./movies").stdin("s").stdout(".*1.*2.*3.*4.*", regex=True) \
                           .stdin("1", prompt=False).stdout(".*", regex = True) \
                           .stdin("star", prompt=False).stdout(".*1", regex=True) \
                           .stdin("e").exit(0)