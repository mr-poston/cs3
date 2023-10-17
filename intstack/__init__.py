import check50

@check50.check()
def exists():
    """IntStack.java exists"""
    check50.exists("IntStack.java")

@check50.check()
def compiles():
    """IntStack.java compiles"""
    check50.run("javac IntStack.java").exit(0)

@check50.check()
def default_constructor():
    """A default constructor exists"""
    f = open("IntStack.java", "r")
    content = f.read()
    if "public IntStack()" not in content:
        raise check50.Failure("Missing the default constructor!")
    
@check50.check()
def param_constructor():
    """A one-parameter constructor exists"""
    f = open("IntStack.java", "r")
    content = f.read()
    if "public IntStack(int " not in content:
        raise check50.Failure("Missing the one-parameter constructor!")
    
@check50.check()
def private_double_capacity():
    """private doubleCapacity method exists"""
    f = open("IntStack.java", "r")
    content = f.read()
    if "private void doubleCapacity()" not in content:
        raise check50.Failure("Must have private void doubleCapacity() method!")
    
@check50.check()
def check_push():
    """push and size methods work"""
    check50.run("java IntStack").stdout("4").exit(0)
    
@check50.check()
def check_empty_1():
    """isEmpty method works when stack is not empty"""
    check50.run("java IntStack 1 2 3 empty").stdout("false").exit(0)

@check50.check()
def check_empty_2():
    """isEmpty method works when stack is empty"""
    check50.run("java IntStack empty").stdout("true").exit(0)

@check50.check()
def check_to_string():
    """toString method works"""
    check50.run("java IntStack 1 2 3").stdout("[1, 2, 3]").exit(0)

@check50.check()
def check_pop():
    """pop method removes and returns the top item from the stack"""
    check50.run("java IntStack 1 2 3 pop").stdout("3\n2").exit(0)

@check50.check()
def check_peek():
    "peek method returns but does not remove the top item from the stack"
    check50.run("java IntStack 1 2 3 peek").stdout("3\n3").exit(0)

@check50.check()
def check_exception():
    """pop throws EmptyStackException for empty stack"""
    check50.run("java IntStack 1 2 3 exception").stdout("OOPS! Stack is empty: can't pop()").exit(0)