import check50

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
    magic_lines = []
    output = check50.run("./magic").stdout()
    output = output.lower()
    lines = output.split("\n")
    for line in lines:
        if "magic" in line:
            magic_lines.append(line)
    for i in range(len(magic_lines)):
        if 0 <= i < 3:
            if "not" in magic_lines[i]:
                raise check50.Failure("The first three squares should be magic! Make sure your output indicates that.")
        elif "not" not in magic_lines[i]:
            raise check50.Failure("The last four squares should NOT be magic! Make sure your output indicates that.")
