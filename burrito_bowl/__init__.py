import check50

@check50.check()
def exists():
    """burrito_bowl.cpp exists"""
    check50.exists("burrito_bowl.cpp")

@check50.check(exists)
def compiles():
    """burrito_bowl.cpp compiles"""
    check50.run("make burrito_bowl").exit(0)

@check50.check(compiles)
def test1():
    """Function prototype"""
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
                if not ("rice," in line and "beans," in line and "salsa," in line):
                    raise check50.Failure("Make sure you don't use default values in your function definition\n" + line)
                        