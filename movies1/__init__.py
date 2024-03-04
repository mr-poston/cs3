import check50

def get_contents():
    with open("movies.cpp", "r") as file:
        return file.read()

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
    """Struct contains correct members"""
    contents = get_contents()
    start = contents.index("struct movie")
    limit = contents.index("};") + 2
    struct = contents[start:limit]
    if not (struct.count("string") == 2 and "int" in struct and ("double" in struct or "float" in struct)):
        raise check50.Failure("The movie struct should have 4 members: a string title, a string actor, an int year, and a double rating.")

@check50.check(compiles)
def test2():
    """Adding a movie then listing works"""
    output = check50.run("./movies").stdin("a").stdin("Star Wars").stdin("Ford, Harrison").stdin("1977").stdin("9.7").stdin("l").stdin("e", prompt=False).stdout()
    lines = output.split("\n")
    if "Star Wars" not in lines[0]:
        raise check50.Failure("Movie title should be printed first")
    if "Ford, Harrison" not in lines[1]:
        raise check50.Failure("Actor should be printed second\n" + "\n".join(lines))
    if "1977" not in lines[2]:
        raise check50.Failure("Year should be printed third")
    if "9.7" not in lines[3]:
        raise check50.Failure("Rating should be printed fourth")

@check50.check(compiles)
def test3():
    """An input of `e` ends the program"""
    check50.run("./movies").stdin("l").stdin("e").stdout("").exit(0)