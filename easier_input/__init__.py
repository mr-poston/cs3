import check50

@check50.check()
def exists():
    """easier_input.cpp exists"""
    check50.exists("easier_input.cpp")

@check50.check(exists)
def compiles():
    """easier_input.cpp compiles"""
    check50.run("make easier_input").exit(0)

@check50.check(compiles)
def test1():
    """Works when user enters valid input"""
    check50.run("./easier_input").stdin("hello", prompt=True).stdout(".*hello", regex=True) \
                                .stdin("3.14", prompt=True).stdout(".*3.14", regex=True) \
                                .stdin("0.5", prompt=True).stdout(".*0.5", regex=True) \
                                .stdin("22", prompt=True).stdout(".*22", regex=True) \
                                .stdin("3", prompt=True).stdout(".*3", regex=True).exit(0)

@check50.check(compiles)
def test2():
    """Works when user enters an out of range double"""
    check50.run("./easier_input").stdin("hello", prompt=True).stdout(".*hello", regex=True) \
                                .stdin("3.14", prompt=True).stdout(".*3.14", regex=True) \
                                .stdin("3.4", prompt=True).stdin("0.5", prompt=True).stdout(".*0.5", regex=True) \
                                .stdin("22", prompt=True).stdout(".*22", regex=True) \
                                .stdin("3", prompt=True).stdout(".*3", regex=True).exit(0)
                                
@check50.check(compiles)
def test3():
    """Works when user enters an out of range int"""
    check50.run("./easier_input").stdin("hello", prompt=True).stdout(".*hello", regex=True) \
                                .stdin("3.14", prompt=True).stdout(".*3.14", regex=True) \
                                .stdin("0.5", prompt=True).stdout(".*0.5", regex=True) \
                                .stdin("22", prompt=True).stdout(".*22", regex=True) \
                                .stdin("18", prompt=True).stdin("3", prompt=True).stdout(".*3", regex=True).exit(0)

@check50.check(exists)
def test4():
    """inputLine function exists"""
    f = open("easier_input.cpp", "r")
    contents = f.read()
    lines = contents.split("\n")
    found = False
    for line in lines:
        if "inputLine" in line:
            found = True
            while " " in line:
                line = line.replace(" ", "")
            if "stringinputLine(string" not in line:
                raise check50.Failure("function header should be:\nstring inputLine(string prompt)")
            break
    if not found:
        raise check50.Failure("could not find inputLine function")

@check50.check(exists)
def test5():
    """inputDouble function exists"""
    f = open("easier_input.cpp", "r")
    contents = f.read()
    lines = contents.split("\n")
    found = False
    for line in lines:
        if "inputDouble" in line and line.count("double") == 1:
            found = True
            while " " in line:
                line = line.replace(" ", "")
            if "doubleinputDouble(string" not in line:
                raise check50.Failure("function header should be:\ndouble inputDouble(string prompt)")
            break
    if not found:
        raise check50.Failure("could not find inputDouble function")

@check50.check(exists)
def test6():
    """inputDouble with min and max function exists"""
    f = open("easier_input.cpp", "r")
    contents = f.read()
    lines = contents.split("\n")
    found = False
    for line in lines:
        if "inputDouble" in line and line.count("double") == 3:
            found = True
            while " " in line:
                line = line.replace(" ", "")
            if "doubleinputDouble(string" not in line:
                raise check50.Failure("function header should be:\ndouble inputDouble(string prompt, double min, double max)")
            break
    if not found:
        raise check50.Failure("could not find inputDouble with min and max function")

@check50.check(exists)
def test7():
    """inputInt function exists"""
    f = open("easier_input.cpp", "r")
    contents = f.read()
    lines = contents.split("\n")
    found = False
    for line in lines:
        if "inputInt" in line and line.count("int") == 1:
            found = True
            while " " in line:
                line = line.replace(" ", "")
            if "intinputInt(string" not in line:
                raise check50.Failure("function header should be:\nint inputInt(string prompt)")
            break
    if not found:
        raise check50.Failure("could not find inputInt function")

@check50.check(exists)
def test8():
    """inputInt with min and max function exists"""
    f = open("easier_input.cpp", "r")
    contents = f.read()
    lines = contents.split("\n")
    found = False
    for line in lines:
        if "inputInt" in line and line.count("int") == 3:
            found = True
            while " " in line:
                line = line.replace(" ", "")
            if "intinputInt(string" not in line:
                raise check50.Failure("function header should be:\nint inputDouble(string prompt, int min, int max)")
            break
    if not found:
        raise check50.Failure("could not find inputInt with min and max function")