import check50

@check50.check()
def exists():
    """encryption.cpp exists"""
    check50.exists("encryption.cpp")

@check50.check(exists)
def compiles():
    """encryption.cpp compiles"""
    check50.run("make encryption").exit(0)

@check50.check(compiles)
def test1():
    """Correctly shifts 'test' by 15"""
    correct = "ITHI"
    output = check50.run("./encryption").stdin("test e 15", prompt=True).stdout()
    if output.toupper() != correct:
        raise check50.Failure("Output should be:\n" + correct)