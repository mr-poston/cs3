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
def compiles1():
    """Gem.java compiles"""
    check50.run("javac Gem.java").exit(0)

@check50.check()
def compiles2():
    """GemList.java compiles"""
    check50.run("javac GemList.java").exit(0)

@check50.check()
def gem():
    """main method from Gem produces correct output"""
    desired = "GREEN 10, GREEN, 10"
    desired += "\nBLUE 20, BLUE, 20"
    desired += "\nORANGE 30, ORANGE, 30"
    output = check50.run("java Gem").stdout()
    if (output != desired):
        raise check50.Failure("main method from Gem does not produce correct output")