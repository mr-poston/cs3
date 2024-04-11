import check50

def get_magic_lines(output):
    magic_lines = []
    output = output.lower()
    lines = output.split("\n")
    for line in lines:
        if "magic" in line:
            magic_lines.append(line)
    return magic_lines

@check50.check()
def exists():
    """magic.cpp exists"""
    check50.exists("magic.cpp")

@check50.check()
def util_exists():
    """util.cpp and util.h exist"""
    check50.exists("util.cpp")
    check50.exists("util.h")

@check50.check(exists)
def compiles():
    """Code compiles"""
    check50.run("make magic").exit(0)

@check50.check()
def test1():
    """3 magic squares followed by 4 not-magic squares"""
    output = check50.run("./magic").stdout()
    magic_lines = get_magic_lines(output)
    for i in range(len(magic_lines)):
        if 0 <= i < 3:
            if "not" in magic_lines[i]:
                raise check50.Failure("The first three squares should be magic! Make sure your output indicates that.")
        elif "not" not in magic_lines[i]:
            raise check50.Failure("The last four squares should NOT be magic! Make sure your output indicates that.")

@check50.check()
def test2():
    """Everything in square 1 sums to 15"""
    output = check50.run("./magic").stdout()
    magic_lines = get_magic_lines(output)
    if "15" not in magic_lines[0]:
        raise check50.Failure("Everything in square 1 should sum to 15! Make sure your output indicates that.")

@check50.check()
def test3():
    """Everything in square 2 sums to 175"""
    output = check50.run("./magic").stdout()
    magic_lines = get_magic_lines(output)
    if "175" not in magic_lines[1]:
        raise check50.Failure("Everything in square 2 should sum to 175! Make sure your output indicates that.")

@check50.check()
def test4():
    """Everything in square 3 sums to 102"""
    output = check50.run("./magic").stdout()
    magic_lines = get_magic_lines(output)
    if "102" not in magic_lines[2]:
        raise check50.Failure("Everything in square 3 should sum to 102! Make sure your output indicates that.")