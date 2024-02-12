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
    check50.run("./easier_input").stdin("hello", prompt=True).stdout(".*hello", regex=True) \
                                .stdin("3.14", prompt=True).stdout(".*3.14", regex=True) \
                                .stdin("0.5", prompt=True).stdout(".*0.5", regex=True) \
                                .stdin("22", prompt=True).stdout(".*22", regex=True) \
                                .stdin("3", prompt=True).stdout(".*3", regex=True).exit(0)

@check50.check(compiles)
def test2():
    """Works when user enters an out of range double"""
    check50.run("./easier_input").stdin("hello", prompt=True).stdout(".*hello", regex=True) \
                                .stdin("3.14", prompt=True).stdout(".*3.14", regex=True) \
                                .stdin("3.4", prompt=True).stdin("0.5", prompt=True).stdout(".*0.5", regex=True) \
                                .stdin("22", prompt=True).stdout(".*22", regex=True) \
                                .stdin("3", prompt=True).stdout(".*3", regex=True).exit(0)
                                
@check50.check(compiles)
def test3():
    """Works when user enters an out of range int"""
    check50.run("./easier_input").stdin("hello", prompt=True).stdout(".*hello", regex=True) \
                                .stdin("3.14", prompt=True).stdout(".*3.14", regex=True) \
                                .stdin("0.5", prompt=True).stdout(".*0.5", regex=True) \
                                .stdin("22", prompt=True).stdout(".*22", regex=True) \
                                .stdin("18", prompt=True).stdin("3", prompt=True).stdout(".*3", regex=True).exit(0)