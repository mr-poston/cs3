import check50

def get_file_lines(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content.split("\n")

@check50.check()
def exists():
    """pig.cpp exists"""
    check50.exists("pig.cpp")

@check50.check()
def util_exists():
    """util.cpp and util.h exist"""
    check50.exists("util.cpp")
    check50.exists("util.h")

@check50.check(exists)
def compiles():
    """Code compiles"""
    check50.run("make pig").exit(0)

@check50.check()
def test1():
    raise check50.Failure("This test failed because Mr. Poston's test code is incomplete. Please try again later!")