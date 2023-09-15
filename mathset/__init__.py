import check50

@check50.check()
def exists1():
    """MathSet.java exists"""
    check50.exists("MathSet.java")

@check50.check(exists1)
def class_compiles():
    """MathSet.java compiles"""
    check50.run("javac MathSet.java").exit(0)

@check50.check()
def file_check():
    """Reads from mathsetdata.dat correctly"""
    check50.run("java Tester filetest mathsetdata.dat").stdout("Set one \[1, 2, 3, 4, 5\]\nSet two \[4, 5, 6, 7, 8\]\s*", regex=True).exit(0)

@check50.check()
def default():
    """default constructor works"""
    check50.run("java Tester").stdout("Set one \[\]\nSet two \[\]\s*", regex=True).exit(0)

@check50.check()
def union():
    """union() works"""
    one = "1 2 3 4 5"
    two = "4 5 6 7 8"
    check50.run("java Tester union \"1 2 3 4 5\" \"4 5 6 7 8\"").stdout("\[1, 2, 3, 4, 5, 6, 7, 8\]\s*", regex=True).exit(0)

@check50.check()
def intersection():
    """intersection() works"""
    one = "1 2 3 4 5"
    two = "4 5 6 7 8"
    check50.run("java Tester intersection \"1 2 3 4 5\" \"4 5 6 7 8\"").stdout("\[4, 5\]\s*", regex=True).exit(0)

@check50.check()
def differenceAMinusB():
    """differenceAMinusB() works"""
    one = "1 2 3 4 5"
    two = "4 5 6 7 8"
    check50.run("java Tester differenceAMinusB \"1 2 3 4 5\" \"4 5 6 7 8\"").stdout("\[1, 2, 3\]\s*", regex=True).exit(0)

@check50.check()
def differenceBMinusA():
    """differenceBMinusA() works"""
    one = "1 2 3 4 5"
    two = "4 5 6 7 8"
    check50.run("java Tester differenceBMinusA \"1 2 3 4 5\" \"4 5 6 7 8\"").stdout("\[6, 7, 8\]\s*", regex=True).exit(0)

@check50.check()
def symmetricDifference():
    """symmetricDifference() works"""
    one = "1 2 3 4 5"
    two = "4 5 6 7 8"
    check50.run("java Tester symmetricDifference \"1 2 3 4 5\" \"4 5 6 7 8\"").stdout("\[1, 2, 3, 6, 7, 8\]\s*", regex=True).exit(0)

@check50.check()
def disjoint():
    """All methods work for a disjoint set"""
    one = "1 2 3"
    two = "4 5 6"
    check50.run("java Tester union \"1 2 3\" \"6 7 8\"").stdout("\[1, 2, 3, 4, 5, 6\]\s*", regex=True).exit(0)
    check50.run("java Tester intersection \"1 2 3\" \"6 7 8\"").stdout("\[\]\s*", regex=True).exit(0)
    check50.run("java Tester differenceAMinusB \"1 2 3\" \"6 7 8\"").stdout("\[1, 2, 3\]\s*", regex=True).exit(0)
    check50.run("java Tester differenceBMinusA \"1 2 3\" \"6 7 8\"").stdout("\[4, 5, 6\]\s*", regex=True).exit(0)
    check50.run("java Tester symmetricDifference \"1 2 3\" \"6 7 8\"").stdout("\[1, 2, 3, 4, 5, 6\]\s*", regex=True).exit(0)