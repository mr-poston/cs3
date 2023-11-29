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
    output = "GREEN 10, GREEN, 10"
    output += "\nBLUE 20, BLUE, 20"
    output += "\nORANGE 30, ORANGE, 30"
    check50.run("java Gem").stdout(output).exit(0)