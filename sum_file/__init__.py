import check50

def get_contents():
    with open("sum_file.cpp", "r") as file:
        return file.read()

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
    """Produces correct output when file fails to open and exits with a code of 1"""
    check50.run("./sum_file").stdin("blah.txt").stdout("Error: file didn't open").exit(1)

@check50.check(exists)
def test4():
    """You did not hard code the answer!"""
    contents = get_contents()
    if "391787" in contents or "10" in contents:
        raise check50.Failure("Your source code should not contain any numbers other than `0` and `1`")