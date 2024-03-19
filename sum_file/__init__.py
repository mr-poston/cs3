import check50

@check50.check()
def exists():
    """sum_file.cpp exists"""
    check50.exists("sum_file.cpp")

@check50.check()
def existsf():
    """example1.txt and example2.txt exist"""
    check50.exists("example1.txt")
    check50.exists("example2.txt")

@check50.check(exists)
def compiles():
    """sum_file.cpp compiles"""
    check50.run("make sum_file").exit(0)

@check50.check(exists)
def test1():
    """Executing with example2.txt produces a result of 10"""
    check50.run("./sum_file").stdin("example1.txt").stdout("The sum is 10").exit(0)

@check50.check(exists)
def test2():
    """Executing with example1.txt produces the correct sum"""
    check50.run("./sum_file").stdin("example2.txt").stdout("The sum is 391787").exit(0)

@check50.check(exists)
def test3():
    """Produces correct output when file fails to open"""
    check50.run("./sum_file").stdin("blah.txt").stdout("Error: file didn't open").exit(0)