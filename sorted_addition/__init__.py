import check50

@check50.check()
def exists():
    """sorted_addition.cpp exists"""
    check50.exists("sorted_addition.cpp")

@check50.check(exists)
def compiles():
    """sorted_addition.cpp compiles"""
    check50.run("make sorted_addition").exit(0)

@check50.check(compiles)
def test1():
    """Works for input 4 2 7 10 -1"""
    check50.run("./sorted_addition").stdin("4", prompt=True) \
                                    .stdin("2", prompt=True) \
                                    .stdin("7", prompt=True) \
                                    .stdin("10", prompt=True) \
                                    .stdin("-1", prompt=True) \
                                    .stdout("2\n4\n7\n10").exit(0)

@check50.check(compiles)
def test2():
    """Works for input 3 2 1 -1"""
    check50.run("./sorted_addition").stdin("3", prompt=True) \
                                    .stdin("2", prompt=True) \
                                    .stdin("1", prompt=True) \
                                    .stdin("-1", prompt=True) \
                                    .stdout("1\n2\n3\n").exit(0)

@check50.check(exists)
def test3():
    """The correct iterator exists"""
    f = open("sorted_addition.cpp", "r")
    contents = f.read()
    if "vector<int>::iterator " not in contents:
        raise check50.Failure("Your code must include a vector<int>::iterator")

@check50.check(exists)
def test4():
    """The substring 'sort' cannot be found anywhere in your code"""
    f = open("sorted_addition.cpp", "r")
    contents = f.read()
    if "sort" in contents:
        raise check50.Failure("Your code must not include the substring \"sort\"")