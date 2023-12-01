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