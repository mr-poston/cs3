import check50

@check50.check()
def exists():
    """burrito_bowl.cpp exists"""
    check50.exists("burrito_bowl.cpp")

@check50.check(exists)
def compiles():
    """burrito_bowl.cpp compiles"""
    check50.run("make burrito_bowl").exit(0)

@check50.check(exists)
def test1():
    """Correct function prototype and definition"""
    found_prototype = False
    with open("burrito_bowl.cpp") as file:
        content = file.read()
        lines = content.split("\n")
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                continue
            line = line.replace(" ", "")
            if line[:4] == "void" and line[-1] == ";" and "burritoBowl" in line:
                if not ('rice="white"' in line and 'beans="black"' in line and 'salsa="mild"' in line):
                    raise check50.Failure("Your function prototype does not look right")
                else:
                    found_prototype = True
                continue
            if line[:4] == "void" and line[-1] != ";" and "burritoBowl" in line:
                if not found_prototype:
                    raise check50.Failure("You need to declare a function prototype before its definition")
                if "rice=" in line or "beans=" in line or "salsa=" in line:
                    raise check50.Failure("Make sure you don't use default values in your function definition")

@check50.check(exists)
def test2():
    """Correct function calls"""
    chicken = False
    steak = False
    veggie = False
    with open("burrito_bowl.cpp", "r") as file:
        content = file.read()
        lines = content.split("\n")
        for line in lines:
            line = line.strip()
            line = line.replace(" ", "")
            if line == 'burritoBowl("chicken");':
                chicken = True
            if line == 'burritoBowl("steak","white","refried","hot");':
                steak = True
            if line == 'burritoBowl("veggie","brown");':
                veggie = True
    if not (chicken and steak and veggie):
        raise check50.Failure("Make sure your function calls use default values when possible!")

@check50.check(compiles)
def test3():
    """Output matches sample from directions"""
    chicken = False
    steak = False
    veggie = False
    output = check50.run("./burrito_bowl").stdout()
    lines = output.split("\n")
    for line in lines:
        if "chicken" in line and "white rice" in line and "mild salsa" in line:
            chicken = True
        if "steak" in line and "white rice" in line and "hot salsa" in line:
            steak = True
        if "veg" in line and "brown rice" in line and "mild salsa" in line:
            veggie = True
    if not (chicken and steak and veggie):
        message = "Your output should include the following burritos:\n"
        message += "\tA chicken burrito with white rice, black beans, and mild salsa.\n"
        message += "\tA steak burrito with white rice, refried beans, and hot salsa.\n"
        message += "\tA veggie burrito with brown rice, black beans, and mild salsa.\n"
        message += "Your actual output was:\n" + output
        raise check50.Failure(message)
                        