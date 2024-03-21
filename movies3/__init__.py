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
