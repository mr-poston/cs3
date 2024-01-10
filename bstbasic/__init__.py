import check50

desired = "truefalseRoot->10InOrder->36810121416PreOrder->10638141216PostOrder->38612161410ReverseOrder->16141210863Asastring->36810121416"

@check50.check()
def exists():
    """BSTBasic.java exists"""
    check50.exists("BSTBasic.java")

@check50.check()
def compiles():
    """BSTBasic.java compiles"""
    check50.run("javac BSTBasic.java").exit(0)

@check50.check()
def output():
    """Correct Output"""
    output = check50.run("java BSTBasic")
    output = output.replace(" ", "").replace("\n", "")
    if output != desired:
        raise check50.Failure("Your output does not match the desired output")
