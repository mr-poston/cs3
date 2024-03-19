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
def test1():
    """Listing movies works"""
    output = check50.run("./movies").stdin("l").stdin("e", prompt=False).stdout()
    lines = output.split("\n")
    if len(lines) < 2415:
        raise check50.Failure("Your output should list 483 movies!")
    while "" in lines:
        lines.remove("")
    if lines[-2][-3:] != "483":
        raise check50.Failure("Your output should list 483 movies!: " + lines[-2][-3:])

@check50.check(compiles)
def test2():
    """An input of `e` ends the program"""
    check50.run("./movies").stdin("l").stdin("e").stdout("").exit(0)