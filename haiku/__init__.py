import check50

@check50.check()
def exists():
    """haiku.cpp exists"""
    check50.exists("haiku.cpp")

@check50.check()
def compiles():
    """haiku.cpp compiles"""
    check50.run("make haiku").exit(0);

@check50.check()
def cout():
    """Contains `cout`"""
    f = open("haiku.cpp", "r")
    contents = f.read()
    if "cout <<" not in contents:
        raise check50.Failure("You must have cout, a space, and <<")

@check50.check()
def endl():
    """Contains `endl` three times"""
    f = open("haiku.cpp", "r")
    contents = f.read()
    count = 0
    for word in contents:
        if "endl" in word:
            count += 1
    if count < 3:
        raise check50.Failure("You must use endl three times!")

@check50.check()
def is_haiku():
    """Contains three lines with 5, 7, 5 syllables - This will be checked manually!"""