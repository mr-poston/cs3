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
