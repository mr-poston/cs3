import check50

@check50.check()
def exists():
    """BST.java exists"""
    check50.exists("BST.java")

@check50.check()
def compiles():
    """BST.java compiles"""
    check50.run("javac BST.java").exit(0)

@check50.check()
def default_constructor():
    """Default Constructor"""
    check50.run("java BST 0").stdout(" *", regex=True).exit(0)

@check50.check()
def collection_constructor():
    """Collection Constructor"""
    check50.run("java BST 1").stdout(" *1  2  3  4 *", regex=True).exit(0)

@check50.check()
def varags_constructor():
    """Varargs Constructor"""
    check50.run("java BST 2").stdout(" *1  2  3  4 *", regex=True).exit(0)

@check50.check()
def add_check():
    """add method"""
    check50.run("java BST 3").stdout(" *3  6  8  10  12  14  16 *", regex=True).exit(0)

@check50.check()
def contains_check():
    """contains method"""
    check50.run("java BST 4").stdout("true false", regex=False).exit(0)

@check50.check()
def nodes_check(add_check):
    """getNumNodes method"""
    check50.run("java BST 5").stdout("7 8", regex=False).exit(0)

@check50.check()
def leaves_check(add_check):
    """getNumLeaves method"""
    check50.run("java BST 6").stdout("4 4", regex=False).exit(0)

@check50.check()
def levels_check(add_check):
    """getNumLevels method"""
    check50.run("java BST 7").stdout("3 4", regex=False).exit(0)

@check50.check()
def height_check(add_check):
    """getHeight method"""
    check50.run("java BST 8").stdout("2 3", regex=False).exit(0)

@check50.check()
def full_check(add_check):
    """isFull method"""
    check50.run("java BST 9").stdout("true false", regex=False).exit(0)