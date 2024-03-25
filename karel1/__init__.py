import check50

@check50.check()
def exists():
    """buggy.cpp exists"""
    check50.exists("buggy.cpp")

@check50.check(exists)
def compiles():
    """buggy.cpp compiles"""
    check50.run("make buggy").exit(0)