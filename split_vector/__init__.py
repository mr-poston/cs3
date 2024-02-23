import check50

@check50.check()
def exists():
    """split_vector.cpp exists"""
    check50.exists("split_vector.cpp")

@check50.check(exists)
def compiles():
    """split_vector.cpp compiles"""
    check50.run("make split_vector").exit(0)

@check50.check(compiles)
def test1():
    """Prints correct output"""
    check50.run("./split_vector").stdout("8 14 2 6 *\n3 9 5 11 23 *", regex=True).exit(0)

@check50.check(compiles)
def test2():
    """Creates two new int vectors"""
    output = check50.run("./split_vector").stdout()
    if output.count("vector<int>") < 3:
        raise check50.Failure("Make sure to make a vector for evens and a separate vector for odds\n" + str(output.count("vector<int>")))