import check50

@check50.check()
def exists():
    """easier_input.cpp exists"""
    check50.exists("easier_input.cpp")

@check50.check(exists)
def compiles():
    """easier_input.cpp compiles"""
    check50.run("make easier_input").exit(0)

@check50.check(compiles)
def test1():
    """Works when user enters valid input"""
    out1 = "You entered: hello\n"
    out2 = "You entered: 3.14"
    out3 = "You entered: 0.5"
    out4 = "You entered: 22"
    out5 = "You entered: 3"
    check50.run("./easier_input").stdin("hello", prompt=True).stdout(out1) \
                                .stdin("3.14", prompt=True).stdout(out2) \
                                .stdin("0.5", prompt=True).stdout(out3) \
                                .stdin("22", prompt=True).stdout(out4) \
                                .stdin("3", prompt=True).stdout(out5).exit(0)

@check50.check(compiles)
def test2():
    """Works when user enters an out of range double"""
    out1 = "You entered: hello\n"
    out2 = "You entered: 3.14"
    out3 = "You entered: 0.5"
    out4 = "You entered: 22"
    out5 = "You entered: 3"
    check50.run("./easier_input").stdin("hello", prompt=True).stdout(out1) \
                                .stdin("3.14", prompt=True).stdout(out2) \
                                .stdin("3.4", prompt=True).stdin("0.5", prompt=True).stdout(out3) \
                                .stdin("22", prompt=True).stdout(out4) \
                                .stdin("3", prompt=True).stdout(out5).exit(0)
                                
@check50.check(compiles)
def test3():
    """Works when user enters an out of range int"""
    out1 = "You entered: hello\n"
    out2 = "You entered: 3.14"
    out3 = "You entered: 0.5"
    out4 = "You entered: 22"
    out5 = "You entered: 3"
    check50.run("./easier_input").stdin("hello", prompt=True).stdout(out1) \
                                .stdin("3.14", prompt=True).stdout(out2) \
                                .stdin("0.5", prompt=True).stdout(out3) \
                                .stdin("22", prompt=True).stdout(out4) \
                                .stdin("18", prompt=True).stdin("3", prompt=True).stdout(out5).exit(0)