import check50
import re

main = 'public static void main(String[] args)' \
+ '{' \
+ 'IntStack test = new IntStack(2);' \
+ 'try' \
+ '{' \
+ 'test.push(5);' \
+ 'test.push(7);' \
+ 'test.push(9);' \
+ 'System.out.println(test);' \
+ 'System.out.println(test.isEmpty());' \
+ 'System.out.println(test.pop());' \
+ 'System.out.println(test.peek());' \
+ 'System.out.println(test.pop());' \
+ 'System.out.println(test.pop());' \
+ '// Should throw exception' \
+ 'System.out.println(test.pop());' \
+ '}' \
+ 'catch (EmptyStackException e)' \
+ '{' \
+ 'System.out.println(\"OOPS! Stack is empty: can\'t pop() or peek()\");' \
+ '}' \
+ 'System.out.println(test.isEmpty());' \
+ 'System.out.println(test);' \
+ '}}'

@check50.check()
def exists():
    """IntStack.java exists"""
    check50.exists("IntStack.java")

@check50.check()
def compiles():
    """IntStack.java compiles"""
    check50.run("javac IntStack.java").exit(0)

@check50.check()
def original_main():
    """The main method has not been changed"""
    f = open("IntStack.java", "r")
    contents = ""
    to_add = False
    lines = f.readlines()
    for line in lines:
        if "public static void main" in line:
            to_add = True
        if to_add:
            contents += line.strip()
    if contents != main:
        raise check50.Failure(main + "\n---\n" + contents)

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
    """First line of output is "[5, 7, 9]" """
    output = check50.run("java IntStack").stdout()
    if not re.match("[5, 7, 9].*", output, re.S):
        raise check50.Failure("First line should be [5, 7, 9] - try checking push or toString")
    
@check50.check()
def check_empty_1():
    """isEmpty method works when stack is not empty"""
    check50.run("java IntStack").stdout(".*\nfalse.*", regex=True)

@check50.check()
def check_empty_2():
    """isEmpty method works when stack is empty"""
    check50.run("java IntStack").stdout(".*\n.*\n.*\n.*\n.*\n.*\n.*\ntrue.*", regex=True)
