import check50

def get_contents():
    with open("next_birthday.cpp", "r") as file:
        return file.read()

@check50.check()
def exists():
    """next_birthday.cpp exists"""
    check50.exists("next_birthday.cpp")

@check50.check(exists)
def compiles():
    """next_birthday.cpp compiles"""
    check50.run("make next_birthday").exit(0)

@check50.check(exists)
def test1():
    """Refuses non-integer age input"""
    check50.run("./next_birthday").stdin("teenager").stdout("Please enter a valid number.").stdin("10").stdout(".?", regex=True).exit(0)

@check50.check(exists)
def test2():
    """Refuses age input less than 2"""
    check50.run("./next_birthday").stdin("1").stdout("Age invalid. Too young.").stdin("10").stdout(".?", regex=True).exit(0)

@check50.check(exists)
def test3():
    """Refuses age input greater than 110"""
    check50.run("./next_birthday").stdin("111").stdout("Age invalid. Too old.").stdin("10").stdout(".?", regex=True).exit(0)

@check50.check(exists)
def test4():
    """Correctly states age at next birthday"""
    output = check50.run("./next_birthday").stdin("10").stdout()
    if " 11 " not in output:
        raise check50.Failure("Should output a message with an age 1 year beyond the age from the input. (i.e. input of 10 should include 11 in the output)")

@check50.check(exists)
def test5():
    """Throws 'Age invalid. Too young.' for age input less than 2"""
    contents = get_contents()
    if "throw\"Ageinvalid.Tooyoung.\";" not in contents.replace(" ", ""):
        raise check50.Failure("Make sure your code throws \"Age invalid. Too young.\" if age is less than 2")
    lines = contents.split("\n")
    for i in range(len(lines)):
        if "if(age<2)" in lines[i].replace(" ", "") or "if(age<=1)" in lines[i].replace(" ", ""):
            next_line = lines[i + 1]
            if "{" not in lines[i]:
                next_line = lines[i + 2]
            if "throw\"Ageinvalid.Tooyoung.\";" not in next_line.replace(" ", ""):
                raise check50.Failure("Make sure your code throws \"Age invalid. Too young.\" if age is less than 2")

@check50.check(exists)
def test6():
    """Throws 'Age invalid. Too old.' for age input greater than 110"""
    contents = get_contents()
    if "throw\"Ageinvalid.Tooold.\";" not in contents.replace(" ", ""):
        raise check50.Failure("Make sure your code throws \"Age invalid. Too old.\" if age is greater than 110")
    lines = contents.split("\n")
    for i in range(len(lines)):
        if "if(age>110)" in lines[i].replace(" ", "") or "if(age>=111)" in lines[i].replace(" ", ""):
            next_line = lines[i + 1]
            if "{" not in lines[i]:
                next_line = lines[i + 2]
            if "throw\"Ageinvalid.Tooold.\";" not in next_line.replace(" ", ""):
                raise check50.Failure("Make sure your code throws \"Age invalid. Too old.\" if age is greater than 110")

@check50.check(exists)
def test7():
    """Catches invalid_argument"""
    contents = get_contents()
    if "catch(invalid_argument)" not in contents.replace(" ", ""):
        raise check50.Failure("Make sure you catch an invalid argument for non-integer age input")

@check50.check(exists)
def test8():
    """Catches custom string message"""
    contents = get_contents()
    if "catch(constchar*" not in contents.replace(" ", ""):
        raise check50.Failure("Make sure you catch custom string literals for invalid age range")