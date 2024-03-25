import check50

@check50.check()
def exists():
    """movies.cpp exists"""
    check50.exists("movies.cpp")

@check50.check(exists)
def compiles():
    """movies.cpp compiles"""
    check50.run("make movies").exit(0)

# @check50.check(exists)
# def test0():
#     raise check50.Failure("This test failed because the tests are incomplete. Please try again later.")

@check50.check(compiles)
def test1():
    """Search by title"""
    check50.run("./movies").stdin("s").stdout(".*1.*2.*3.*4.*", regex=True) \
                           .stdin("1", prompt=False).stdout(".*", regex = True) \
                           .stdin("star", prompt=False).stdout(".*1", regex=True) \
                           .stdin("e").exit(0)

@check50.check(compiles)
def test2():
    """Search rejects non-integer input"""
    check50.run("./movies").stdin("s").stdout(".*1.*2.*3.*4.*", regex=True) \
                           .stdin("title", prompt=False).stdout(".*", regex = True) \
                           .stdin("1", prompt=False).stdout(".*", regex = True) \
                           .stdin("star", prompt=False).stdout(".*1", regex=True) \
                           .stdin("e").exit(0)

@check50.check(compiles)
def test3():
    """Search rejects integer input other than 1, 2, 3, or 4"""
    check50.run("./movies").stdin("s").stdout(".*1.*2.*3.*4.*", regex=True) \
                           .stdin("0", prompt=False).stdout(".*", regex = True) \
                           .stdin("1", prompt=False).stdout(".*", regex = True) \
                           .stdin("star", prompt=False).stdout(".*1", regex=True) \
                           .stdin("e").exit(0)

@check50.check(compiles)
def test4():
    """Search by year"""
    check50.run("./movies").stdin("s").stdout(".*1.*2.*3.*4.*", regex=True) \
                           .stdin("2", prompt=False) \
                           .stdin("2000", prompt=False) \
                           .stdin("2012", prompt=False) \
                           .stdout(".*145", regex=True) \
                           .stdin("e").exit(0)

@check50.check(compiles)
def test5():
    """Search by actor"""
    check50.run("./movies").stdin("s").stdout(".*1.*2.*3.*4.*", regex=True) \
                           .stdin("3", prompt=False) \
                           .stdin("Arnold", prompt=False) \
                           .stdout(".*25", regex=True) \
                           .stdin("e").exit(0)

@check50.check(compiles)
def test6():
    """Search by rating"""
    check50.run("./movies").stdin("s").stdout(".*1.*2.*3.*4.*", regex=True) \
                           .stdin("4", prompt=False) \
                           .stdin("2", prompt=False) \
                           .stdin("4", prompt=False) \
                           .stdout(".*12", regex=True) \
                           .stdin("e").exit(0)