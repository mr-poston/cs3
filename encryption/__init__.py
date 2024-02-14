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
    """Correctly encrypts 'test' with shift of 15"""
    correct = "ITHI"
    output = check50.run("./encryption").stdin("test", prompt=True).stdin("e", prompt=True).stdin("15", prompt=True).stdout()
    if correct not in output:
        raise check50.Failure("Output should contain:\n" + correct + "\tbut was: " + output)

@check50.check(compiles)
def test2():
    """Correctly encrypts 'Hello World!' with shift of 8"""
    correct = "PMTTW EWZTL!"
    output = check50.run("./encryption").stdin("Hello World!", prompt=True).stdin("e", prompt=True).stdin("8", prompt=True).stdout()
    if correct not in output:
        raise check50.Failure("Output should contain:\n" + correct + "\tbut was: " + output)

@check50.check(compiles)
def test3():
    """Correctly encrypts 'I 8 NYC!' with shift of 12"""
    correct = "U 8 ZKO!"
    output = check50.run("./encryption").stdin("I 8 NYC!", prompt=True).stdin("e", prompt=True).stdin("12", prompt=True).stdout()
    if correct not in output:
        raise check50.Failure("Output should contain:\n" + correct + "\tbut was: " + output)

@check50.check(compiles)
def test4():
    """Correctly decrypts 'pbZChGRE' with shift of 13"""
    correct = "COMPUTER"
    output = check50.run("./encryption").stdin("pbZChGRE", prompt=True).stdin("d", prompt=True).stdin("13", prompt=True).stdout()
    if correct not in output:
        raise check50.Failure("Output should contain:\n" + correct + "\tbut was: " + output)

@check50.check(compiles)
def test5():
    """Correctly decrypts 'WTAAD LDGAS!' with shift of 15"""
    correct = "HELLO WORLD"
    output = check50.run("./encryption").stdin("WTAAD LDGAS!", prompt=True).stdin("d", prompt=True).stdin("15", prompt=True).stdout()
    if correct not in output:
        raise check50.Failure("Output should contain:\n" + correct + "\tbut was: " + output)

@check50.check(compiles)
def test6():
    """Correctly decrypts 'ITHI' with shift of 15"""
    correct = "TEST"
    output = check50.run("./encryption").stdin("ITHI", prompt=True).stdin("d", prompt=True).stdin("15", prompt=True).stdout()
    if correct not in output:
        raise check50.Failure("Output should contain:\n" + correct + "\tbut was: " + output)

@check50.check(compiles)
def test7():
    """Correctly decrypts 'ithi' with shift of 15"""
    correct = "TEST"
    output = check50.run("./encryption").stdin("ithi", prompt=True).stdin("d", prompt=True).stdin("15", prompt=True).stdout()
    if correct not in output:
        raise check50.Failure("Output should contain:\n" + correct + "\tbut was: " + output)

@check50.check(compiles)
def test8():
    """Rejects incorrect encrtpt/decrypt choice"""
    output = check50.run("./encryption").stdin("a", prompt=True).stdin("0", prompt=True).stdin("e", prompt=True).stdin("1", prompt=True).stdout()
    if "B" not in output or "Z" not in output:
        raise check50.Failure("uh-oh")

@check50.check(compiles)
def test9():
    """Rejects out of range shift"""
    output = check50.run("./encryption").stdin("a", prompt=True).stdin("e", prompt=True).stdin("99", prompt=True).stdin("1", prompt=True).stdout()
    if "B" not in output or "Z" not in output:
        raise check50.Failure("uh-oh")