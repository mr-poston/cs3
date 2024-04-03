import check50

def get_file_lines(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content.split("\n")

@check50.check()
def exists():
    """patient.cpp exists"""
    check50.exists("patient.cpp")

@check50.check()
def util_exists():
    """util.cpp and util.h exist"""
    check50.exists("util.cpp")
    check50.exists("util.h")

@check50.check(exists)
def compiles():
    """Code compiles"""
    check50.run("make patient").exit(0)

@check50.check()
def test1():
    check50.run("./patient").stdin("David").stdin("98.7") \
                            .stdin("Louise").stdin("99.9") \
                            .stdin("Walter").stdin("90").stdin("108").stdin("97") \
                            .stdin("Jacob").stdin("100.5").stdin("exit") \
                            .stdout(".*DAVID\nLOUISE\nWALTER", regex=True).exit(0)

@check50.check()
def test2():
    check50.run("./patient").stdin("Maria").stdin("95.1").stdin("exit").stdout(".*MARIA", regex=True).exit(0)

@check50.check()
def test3():
    """patient struct exists"""
    lines = get_file_lines("patient.cpp")
    found = False
    for line in lines:
        if "struct patient" in line:
            found = True
    if not found:
        raise check50.Failure("You must have a struct called patient")

@check50.check()
def test4():
    """Vector of patients exists"""
    lines = get_file_lines("patient.cpp")
    found = False
    for line in lines:
        if "vector<patient>" in line:
            found = True
    if not found:
        raise check50.Failure("You must use a vector of `patient`s")

@check50.check()
def test5():
    """Use of readLine"""
    lines = get_file_lines("patient.cpp")
    found = False
    for line in lines:
        if "readLine(\"" in line.replace(" ", ""):
            found = True
    if not found:
        raise check50.Failure("You must use the readLine function from the util library")

@check50.check()
def test6():
    """Use of toUpperCase"""
    lines = get_file_lines("patient.cpp")
    found = False
    for line in lines:
        if "toUpperCase(" in line.replace(" ", ""):
            found = True
    if not found:
        raise check50.Failure("You must use the toUpperCase function from the util library")

@check50.check()
def test7():
    """Use of readDouble"""
    lines = get_file_lines("patient.cpp")
    found = False
    for line in lines:
        if "readDouble(" in line.replace(" ", ""):
            found = True
    if not found:
        raise check50.Failure("You must use the readDouble function from the util library")


    