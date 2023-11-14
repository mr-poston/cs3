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
def private_class():
    """private class ListNode exists"""
    f = open("MyLinkedList.java", "r")
    content = f.read()
    if "private class ListNode" not in content:
        raise check50.Failure("Must have private class ListNode!")

@check50.check()
def default_constructor():
    """A default constructor exists"""
    f = open("MyLinkedList.java", "r")
    content = f.read()
    if "public MyLinkedList()" not in content:
        raise check50.Failure("Missing the default constructor!")
    
@check50.check()
def check_toString():
    """toString method works when list is empty"""
    check50.run("java MyLinkedList toString").stdout("[]").exit(0)
    
@check50.check()
def check_addToEmpty():
    """addToEmpty works"""
    check50.run("java MyLinkedList addToEmpty").stdout("[2]").exit(0)

@check50.check()
def check_empty_2():
    """addToEnd works"""
    check50.run("java MyLinkedList addToEnd").stdout("[2, 75]").exit(0)

@check50.check()
def check_add():
    """adding to a valid index works"""
    check50.run("java MyLinkedList add").stdout("[2, 21, 19, 75]").exit(0)

@check50.check()
def check_addOutOfBounds():
    """attempting to add to an invalid index throws IndexOutOfBoundsException"""
    check50.run("java MyLinkedList addOutOfBounds").stdout("Out of Bounds").exit(0)

@check50.check()
def check_print():
    "peek method returns but does not remove the front item from the queue"
    check50.run("java MyLinkedList print").stdout("2 21 19 75 *", regex=True).exit(0)

@check50.check()
def check_removeFromBeginning():
    """removeFromBeginning works"""
    check50.run("java MyLinkedList removeFromBeginning").stdout("[21, 19, 75]").exit(0)

@check50.check()
def check_remove():
    """removing from a valid index works"""
    check50.run("java MyLinkedList remove").stdout("[2, 21, 75]").exit(0)

@check50.check()
def check_removeOutOfBoounds():
    """removeFromBeginning works"""
    check50.run("java MyLinkedList removeOutOfBounds").stdout("Out of Bounds").exit(0)
