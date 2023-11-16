import check50

@check50.check()
def exists():
    """MyLinkedList.java exists"""
    check50.exists("MyLinkedList.java")

@check50.check()
def compiles():
    """MyLinkedList.java compiles"""
    check50.run("javac MyLinkedList.java").exit(0)

@check50.check()
def holds_strings():
    """MyLinked List can store String objects"""
    check50.run("java MyLinkedList String").stdout("[hello1, hello2, hello3]").exit(0)

@check50.check()
def holds_doubles():
    """MyLinked List can store String objects"""
    check50.run("java MyLinkedList Double").stdout("[3.14, 1.41, 1.61, 0.5]").exit(0)

@check50.check()
def add_to_front():
    """Correctly adds an item at index 0 of a list that already has items"""
    check50.run("java MyLinkedList AddToFront").stdout("[9.12, 3.14, 1.41, 1.61, 0.5]").exit(0)

@check50.check()
def size_method():
    """size method returns correct size"""
    check50.run("java MyLinkedList Size").stdout("Test1 size: 3\nTest2 size: 4").exit(0)