import check50

@check50.check()
def exists():
    """change.cpp exists"""
    check50.exists("change.cpp")

@check50.check()
def compiles():
    """change.cpp compiles"""
    check50.run("make change").exit(0);

@check50.check()
def test1():
    """Works for 436"""
    check50.run("./change").stdin("436", prompt=True).stdout("\n[Qq].*17\n[Dd].*1\n[Nn].*0\n[Pp].*1", regex=True).exit(0)