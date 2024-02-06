import check50

@check50.check()
def exists():
    """fast_food.cpp exists"""
    check50.exists("fast_food.cpp")

@check50.check()
def compiles():
    """fast_food.cpp compiles"""
    check50.run("make fast_food").exit(0)

@check50.check()
def test1():
    """Works for input 1 sandwich, 2 fries, and 2 sodas"""
    check50.run("./fast_food").stdin("1", prompt=True).stdin("2", prompt=True).stdin("2", prompt=True).stdout(".*\$11\.50\n.*\$0\.95\n.*\$12\.45\n", regex=True).exit(0)

@check50.check()
def test2():
    """Works for input 2 sandwiches, 1 fries, and 1 sodas"""
    check50.run("./fast_food").stdin("2", prompt=True).stdin("1", prompt=True).stdin("1", prompt=True).stdout(".*\$11\.60\n.*\$0\.96\n.*\$12\.56\n", regex=True).exit(0)

@check50.check()
def test3():
    """Works for input 3 sandwiches, 0 fries, and 3 sodas"""
    check50.run("./fast_food").stdin("3", prompt=True).stdin("0", prompt=True).stdin("3", prompt=True).stdout(".*\$16\.50\n.*\$1\.36\n.*\$17\.86\n", regex=True).exit(0)
