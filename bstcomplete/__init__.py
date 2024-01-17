import check50

@check50.check()
def exists():
    """BSTComplete.java exists"""
    check50.exists("BSTComplete.java")

@check50.check()
def compiles():
    """BSTComplete.java compiles"""
    check50.run("javac BSTComplete.java").exit(0)

@check50.check()
def no_children():
    """No children"""
    check50.run("java BSTComplete 0").stdout(" *3  6  8  10  14  16 *", regex=True).exit(0)

@check50.check()
def one_child():
    """1 child"""
    check50.run("java BSTComplete 1").stdout(" *3  6  8  10  16 *", regex=True).exit(0)

@check50.check()
def two_children():
    """2 children"""
    check50.run("java BSTComplete 2").stdout(" *3  6  8  12  14  16 *", regex=True).exit(0)