import check50

@check50.check()
def exists():
  """IteratorRemover.java exists"""
  check50.exists("IteratorRemover.java")

@check50.check(exists)
def check0():
  """IteratorRemover.java compiles"""
  check50.run("javac IteratorRemover.java").exit(0)

@check50.check(exists)
def check2():
  """"a b c a b c" becomes [b, c, b, c]"""
  actual = check50.run("java IteratorRemover").stdout()
  if actual.find("[b, c, b, c]") == -1:
    raise check50.Failure(actual)

@check50.check(exists)
def check3():
  """"a b c d e f g h i j x x x x" becomes [a, b, c, d, e, f, g, h, i, j]"""
  actual = check50.run("java IteratorRemover").stdout()
  if actual.find("[a, b, c, d, e, f, g, h, i, j]") == -1:
    raise check50.Failure(actual)

@check50.check(exists)
def check4():
  """"1 2 3 4 5 6 a b c a b c" becomes [1, 2, 3, 4, 5, 6, a, c, a, c]"""
  actual = check50.run("java IteratorRemover").stdout()
  if actual.find("[1, 2, 3, 4, 5, 6, a, c, a, c]") == -1:
    raise check50.Failure(actual)

@check50.check(exists)
def check6():
  """Uses Iterator"""
  f = open("IteratorRemover.java", "r")
  contents = f.read()
  if contents.find(".iterator()") == -1:
    raise check50.Failure("You must use an Iterator!")
