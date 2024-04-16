import check50

@check50.check()
def exists():
    """gradient.cpp exists"""
    check50.exists("gradient.cpp")

@check50.check()
def util_exists():
    """util.cpp and util.h exist"""
    check50.exists("util.cpp")
    check50.exists("util.h")

@check50.check(exists)
def compiles():
    """Code compiles"""
    check50.run("make gradient").exit(0)

@check50.check()
def test1():
    """Width: 5 Height: 4 Seed: 2 Step: 4"""
    output = check50.run("./gradient").stdin("5").stdin("4").stdin("2").stdin("4").stdout()
    output = output.replace("\n", "\t")
    values = output.split("\t")
    numbers = []
    for number in values:
        if type(number) == int:
            numbers.append(int(number))
    num_check = [2,6,10,14,18,6,10,14,18,22,10,14,18,22,26,14,18,22,26,30]
    if numbers != num_check:
        raise check50.Failure(output)