import check50

@check50.check()
def exists():
    """MinHeap.java exists"""
    check50.exists("MinHeap.java")

@check50.check()
def compiles():
    """MinHeap.java compiles"""
    check50.run("javac MinHeap.java").exit(0)

@check50.check()
def empty():
    """Empty Heap"""
    check50.run("java MinHeap 0").stdout("[]").exit(0)

@check50.check()
def one():
    """Add one element"""
    check50.run("java MinHeap 1").stdout("[5]").exit(0)

@check50.check()
def two():
    """Add two elements and swap down"""
    check50.run("java MinHeap 2").stdout("[3, 5]").exit(0);

@check50.check()
def three():
    """Add two elements with varargs constructor"""
    check50.run("java MinHeap 3").stdout("[1, 6, 5, 10]").exit(0);

@check50.check()
def four():
    """Remove and swap up"""
    check50.run("java MinHeap 4").stdout("\n\nPRINTING THE HEAP!"\n\n      2\n     5  7\n   9  10  8  75\n17).exit(0);