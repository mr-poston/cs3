import check50

@check50.check()
def exists():
    """RecursionFun.java exists"""
    check50.exists("RecursionFun.java")

@check50.check()
def compiles():
    """RecursionFun.java compiles"""
    check50.run("javac RecursionFun.java").exit(0)

@check50.check()
def sum_reciprocals():
    """sumReciprocals method works"""
    check50.run("java RecursionFun sumReciprocals").stdout("2.9289682539682538").exit(0)

@check50.check()
def product_of_evens():
    """productOfEvens method works"""
    check50.run("java RecursionFun productOfEvens").stdout("384").exit(0)

@check50.check()
def double_up():
    """doubleUp method works"""
    desired = "[3, 7, 12, 9]\n"
    desired += "[3, 3, 7, 7, 12, 12, 9, 9]"
    check50.run("java RecursionFun doubleUp").stdout(desired).exit(0)

@check50.check()
def count_to_by():
    """countToBy method works"""
    desired = "4, 9, 14, 19, 24, 29, 34\n"
    desired += "1, 5, 9, 13, 17, 21, 25"
    check50.run("java RecursionFun countToBy").stdout(desired).exit(0)

@check50.check()
def matching_digits():
    """matchingDigits method works"""
    desired = "1\n"
    desired += "3"
    check50.run("java RecursionFun matchingDigits").stdout(desired).exit(0)

@check50.check()
def print_this():
    """printThis method works"""
    desired = "*\n"
    desired += "**\n"
    desired += "<*>\n"
    desired += "<**>\n"
    desired += "<<*>>\n"
    desired += "<<**>>\n"
    desired += "<<<*>>>\n"
    desired += "<<<**>>>"
    check50.run("java RecursionFun printThis").stdout(desired).exit(0)

@check50.check()
def print_nums_2():
    """printNums2 method works"""
    desired = "1\n"
    desired += "1 1\n"
    desired += "2 1 2\n"
    desired += "2 1 1 2\n"
    desired += "3 2 1 2 3\n"
    desired += "3 2 1 1 2 3\n"
    desired += "4 3 2 1 2 3 4\n"
    desired += "4 3 2 1 1 2 3 4\n"
    desired += "5 4 3 2 1 2 3 4 5\n"
    desired += "5 4 3 2 1 1 2 3 4 5\n"
    check50.run("java RecursionFun printNums2").stdout(desired).exit(0)