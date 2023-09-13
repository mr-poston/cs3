import check50

@check50.check()
def exists1():
    """OddEvenSets.java exists"""
    check50.exists("OddEvenSets.java")

@check50.check(exists1)
def class_compiles():
    """OddEvenSets.java compiles"""
    check50.run("javac OddEvenSets.java").exit(0)

@check50.check()
def file_check():
    """Reads from oddeven.dat correctly"""
    check50.run("java Tester filetest oddevendata.dat").exit(0)

@check50.check()
def example1():
    """Sorts "1 5 9 4 6 8 12" correctly"""
    check50.run("java Tester \"1 5 9 4 6 8 12\"").stdout("ODDS : [1, 5, 9]\nEVENS : [4, 6, 8, 12]\n\n").exit(0)

@check50.check()
def example2():
    """Sorts "3 5 7 17 29 4 6 56 72" correctly"""
    check50.run("java Tester \"3 5 7 17 29 4 6 56 72\"").stdout("ODDS : [3, 5, 7, 17, 29]\nEVENS : [4, 6, 56, 72]\n\n").exit(0)

@check50.check()
def example3():
    """Sorts "3 6 12 2 28 6" correctly"""
    check50.run("java Tester \"3 6 12 2 28 6\"").stdout("ODDS : [3]\nEVENS : [2, 6, 12, 28]\n\n").exit(0)

@check50.check()
def example4():
    """Sorts "4 4 4 4 4 4 4 4" correctly"""
    check50.run("java Tester \"4 4 4 4 4 4 4 4\"").stdout("ODDS : []\nEVENS : [4]\n\n").exit(0)

@check50.check()
def example5():
    """Sorts "1 1 1 1 1 1 1 1" correctly"""
    check50.run("java Tester \"1 1 1 1 1 1 1 1\"").stdout("ODDS : [1]\nEVENS : []\n\n").exit(0)

@check50.check()
def example6():
    """Sorts "1 2 3 4 5 6 7 8 9" correctly"""
    check50.run("java Tester \"1 2 3 4 5 6 7 8 9\"").stdout("ODDS : [1, 3, 5, 7, 9]\nEVENS : [2, 4, 6, 8]\n\n").exit(0)