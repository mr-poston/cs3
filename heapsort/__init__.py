import check50

@check50.check()
def exists():
    """MinHeap.java exists"""
    check50.exists("MinHeap.java")

@check50.check()
def compiles():
    """MinHeap.java compiles"""
    check50.run("javac MinHeap.java").exit(0)

@check50.check()
def line_1():
    """Correct output for input 99,2,8,75,10,7,9,17,5,3,4,1,11,1"""
    desired = "[1, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 17, 75, 99]"
    output = check50.run("java MinHeap").stdout()
    lines = output.split("\n")
    while "" in lines:
        lines.remove("")
    line1 = lines[0]
    if line1 != desired:
        raise check50.Failure("First line of output should be: " + desired)


@check50.check()
def line_2():
    """Correct output for input -3,28,18,5,3,17,29,6,5,3,4,1,11,1"""
    desired = "[-3, 1, 1, 3, 3, 4, 5, 5, 6, 11, 17, 18, 28, 29]"
    output = check50.run("java MinHeap").stdout()
    lines = output.split("\n")
    while "" in lines:
        lines.remove("")
    line2 = lines[1]
    if line2 != desired:
        raise check50.Failure("Second line of output should be: " + desired)

@check50.check()
def hard_code():
    """You did not hard-code the answer"""
    f = open("MinHeap.java", "r")
    lines = f.read().split("\n")
    first_line = "[1, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 17, 75, 99]"
    second_line = "[-3, 1, 1, 3, 3, 4, 5, 5, 6, 11, 17, 18, 28, 29]"
    cheat = False
    for line in lines:
        if first_line in line:
            cheat = True
            if "//" in line and line.index("//") < line.index(first_line):
                cheat = False
        if second_line in line:
            cheat = True
            if "//" in line and line.index("//") < line.index(second_line):
                cheat = False
    if cheat:
        raise check50.Failure("Don't hard-code the answer, you cheater!")
