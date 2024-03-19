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
    output = "The sum is 10".lower()
    check50.run("./sum_file").stdin("example1.txt").stdout(output).exit(0)

@check50.check(exists)
def test2():
    """Executing with example1.txt produces the correct sum"""
    output = "The sum is 391787".lower()
    check50.run("./sum_file").stdin("example2.txt").stdout(output).exit(0)

@check50.check(exists)
def test3():
    """Produces correct output when file fails to open"""
    output = "Error: file didn't open".lower()
    check50.run("./sum_file").stdin("blah.txt").stdout(output).exit(0)