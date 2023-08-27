import check50

@check50.check()
def exists():
  """IteratorRemover.java exists"""
  check50.exists("IteratorRemover.java")

@check50.check(exists)
def check0():
  """IteratorRemover.java compiles"""
  check50.run("javac IteratorRemover.java").exit(0)

# @check50.check(exists)
# def check2():
#   """Example #1"""
#   actual = check50.run("java IteratorRemover).stdout("[b, c, b, c]", regex=False)
#   if actual.find("[b, c, b, c]") == -1:
#     raise check50.Failure(actual)

# @check50.check(exists)
# def check3():
#   """Example #2"""
#   check50.run("javac Grader.java")
#   check50.run("java Grader \"a b c d e f g h i j x x x x\" \"x\"").stdout("[a, b, c, d, e, f, g, h, i, j]", regex=False).exit(0)

# @check50.check(exists)
# def check4():
#   """Example #3"""
#   check50.run("javac Grader.java")
#   check50.run("java Grader \"1 2 3 4 5 6 a b c a b c\" \"b\"").stdout("[1, 2, 3, 4, 5, 6, a, c, a, c]", regex=False).exit(0)

# @check50.check(exists)
# def check5():
#   """Handles empty list"""
#   check50.run("javac Grader.java")
#   check50.run("java Grader \"\" \"\"").stdout("[]", regex=False).exit(0)

@check50.check(exists)
def check6():
  """Uses Iterator"""
  f = open("IteratorRemover.java", "r")
  contents = f.read()
  if contents.find(".iterator()") == -1:
    raise check50.Failure("You must use an Iterator!")
