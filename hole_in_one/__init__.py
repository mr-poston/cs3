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
def check_HOLE_ones():
    """Correctly inserts `HOLE` in `ones`"""
    check50.run("./hole_in_one").stdin("HOLE", prompt=True).stdin("ones", prompt=True).stdout("onHOLEes").exit(0)

@check50.check()
def check_HOLE_one():
    """Correctly inserts `HOLE` in `one`"""
    check50.run("./hole_in_one").stdin("HOLE", prompt=True).stdin("one", prompt=True).stdout("oHOLEne").exit(0)

@check50.check()
def check_dog_BOT():
    """Correctly inserts `dog` in `BOT`"""
    check50.run("./hole_in_one").stdin("dog", prompt=True).stdin("BOT", prompt=True).stdout("BdogOT").exit(0)
