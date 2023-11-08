import check50

@check50.check()
def exists():
    """IntQueue.java exists"""
    check50.exists("IntQueue.java")

@check50.check()
def compiles():
    """IntQueue.java compiles"""
    check50.run("javac IntQueue.java").exit(0)

@check50.check()
def default_constructor():
    """A default constructor exists"""
    f = open("IntQueue.java", "r")
    content = f.read()
    if "public IntQueue()" not in content:
        raise check50.Failure("Missing the default constructor!")
    
@check50.check()
def param_constructor():
    """A one-parameter constructor exists"""
    f = open("IntQueue.java", "r")
    content = f.read()
    if "public IntQueue(int " not in content:
        raise check50.Failure("Missing the one-parameter constructor!")
    
@check50.check()
def private_double_capacity():
    """private doubleCapacity method exists"""
    f = open("IntQueue.java", "r")
    content = f.read()
    if "private void doubleCapacity()" not in content:
        raise check50.Failure("Must have private void doubleCapacity() method!")
    
@check50.check()
def check_offer():
    """offer and size methods work"""
    check50.run("java IntQueue").stdout("4").exit(0)
    
@check50.check()
def check_empty_1():
    """isEmpty method works when queue is NOT empty"""
    check50.run("java IntQueue 1 2 3 empty").stdout("false").exit(0)

@check50.check()
def check_empty_2():
    """isEmpty method works when queue IS empty"""
    check50.run("java IntQueue empty").stdout("true").exit(0)

@check50.check()
def check_to_string():
    """toString method works"""
    check50.run("java IntQueue 1 2 3").stdout("[1, 2, 3]").exit(0)

@check50.check()
def check_poll():
    """poll method removes and returns the front item from the queue"""
    check50.run("java IntQueue 1 2 3 poll").stdout("1\n2").exit(0)

@check50.check()
def check_peek():
    "peek method returns but does not remove the front item from the queue"
    check50.run("java IntQueue 1 2 3 peek").stdout("1\n1").exit(0)

@check50.check()
def check_exception1():
    """poll returns null for empty queue"""
    check50.run("java IntQueue 1 2 3 badPoll").stdout("null").exit(0)

@check50.check()
def check_exception2():
    """peek returns null for empty queue"""
    check50.run("java IntQueue 1 2 3 badPeek").stdout("null").exit(0)