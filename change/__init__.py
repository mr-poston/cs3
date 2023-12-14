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

@check50.check()
def test2():
    """Works for 93"""
    check50.run("./change").stdin("93", prompt=True).stdout("\n[Qq].*3\n[Dd].*1\n[Nn].*1\n[Pp].*3", regex=True).exit(0)

@check50.check()
def test3():
    """Works for 999"""
    check50.run("./change").stdin("999", prompt=True).stdout("\n[Qq].*39\n[Dd].*2\n[Nn].*0\n[Pp].*4", regex=True).exit(0)

@check50.check()
def negative():
    """Rejects negative input with exit code 1"""
    check50.run("./change").stdin("-5", prompt=True).exit(1)

@check50.check()
def big():
    """Rejects input greater than 999 with exit code 2"""
    check50.run("./change").stdin("2000", prompt=True).exit(2)