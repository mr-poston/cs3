import check50

@check50.check()
def exists():
    """hole_in_one.cpp exists"""
    check50.exists("hole_in_one.cpp")

@check50.check()
def compiles():
    """hole_in_one.cpp compiles"""
    check50.run("make hole_in_one").exit(0);

@check50.check()
def check_middle_even():
    """Correctly inserts word1 in the middle of word2 when word2 has an even number of letters"""
    check50.run("./hole_in_one").stdin("HOLE", prompt=True).stdin("ones", prompt=True).stdout("onHOLEes").exit(0)

@check50.check()
def check_middle_odd():
    """Correctly inserts word1 in the middle of word2 when word2 has an odd number of letters"""
    check50.run("./hole_in_one").stdin("HOLE", prompt=True).stdin("one", prompt=True).stdout("oHOLEne").exit(0)