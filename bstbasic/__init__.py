import check50

@check50.check()
def exists():
    """BSTBasic.java exists"""
    check50.exists("BSTBasic.java")

@check50.check()
def compiles():
    """BSTBasic.java compiles"""
    check50.run("javac BSTBasic.java").exit(0)