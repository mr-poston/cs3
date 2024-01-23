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
def no_children():
    """Empty Heap"""
    check50.run("java MinHeap 0").stdout("[]").exit(0)