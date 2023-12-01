import check50

@check50.check()
def exists1():
    """Gem.java exists"""
    check50.exists("Gem.java")

@check50.check()
def exists2():
    """GemList.java exists"""
    check50.exists("GemList.java")

@check50.check()
def gem():
    """main method from Gem produces correct output"""
    desired = "GREEN 10, GREEN, 10"
    desired += "\nBLUE 20, BLUE, 20"
    desired += "\nORANGE 30, ORANGE, 30"
    check50.run("java Gem").stdout(desired).exit(0)

@check50.check()
def gem_list():
    """main method from GemList produces correct output"""
    desired = "<none>\n\n"
    desired += "size = 0, score = 0\n\n"
    desired += "BLUE\n"
    desired += "size = 1, score = 10\n\n"
    desired += "BLUE -> BLUE\n"
    desired += "size = 2, score = 60\n\n"
    desired += "BLUE -> ORANGE -> BLUE\n"
    desired += "size = 3, score = 60\n\n"
    desired += "BLUE -> ORANGE -> ORANGE -> BLUE\n"
    desired += "size = 4, score = 110\n\n"
    desired += "BLUE -> ORANGE -> ORANGE -> ORANGE -> BLUE\n"
    desired += "size = 5, score = 300\n\n"
    desired += "BLUE -> ORANGE -> GREEN -> ORANGE -> ORANGE -> BLUE\n"
    desired += "size = 6, score = 230"
    check50.run("java GemList").stdout(desired).exit(0)