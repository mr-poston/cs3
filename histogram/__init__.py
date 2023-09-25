import check50

@check50.check()
def exists():
    """Histogram.java exists"""
    check50.exists("Histogram.java")

@check50.check()
def compiles():
    """Histogram.java compiles"""
    check50.run("javac Histogram.java").exit(0);

@check50.check()
def file_check():
    """Reads from histogram.data correctly"""
    output = check50.run("java Histogram").stdout()
    if "a\t**" not in output and "^\t*" not in output:
        raise check50.Failure("Did you forget to print the histograms in the main method?")
    check50.run("java Histogram").exit(0)

@check50.check()
def test_0_contructor():
    """No parameter constructor works"""
    check50.run("java Checker 1").stdout("0", regex=False).exit(0)

@check50.check()
def test_1_constructor():
    """One parameter constructor works"""
    check50.run("java Checker 2").stdout("char\t1---5----01---5\n1\t****\n2\t***\n3\t****\n4\t***\n5\t**\n6\t*\n", regex=False).exit(0)

@check50.check()
def test_set_sentence():
    """putEntry method works"""
    check50.run("java Checker 3").stdout("char\t1---5----01---5\n#\t****\n4\t*\n@\t*\nT\t*\n^\t*\n", regex=False).exit(0)

@check50.check(exists)
def imports():
  """Import statements"""
  f = open("Histogram.java", "r")
  contents = f.read()
  if contents.find("util.*") != -1:
    raise check50.Failure("Import each class separately!!")
  if contents.find("io.*") != -1:
    raise check50.Failure("Import each class separately!!")
  if contents.find("java.io.File;") == -1:
    raise check50.Failure("Did you forget to input File?")
  if contents.find("java.io.IOException;") == -1:
    raise check50.Failure("Did you forget to input IOException?")
  if contents.find("java.util.Map;") == -1:
    raise check50.Failure("Did you forget to input Map?")
  if contents.find("java.util.TreeMap;") == -1:
    raise check50.Failure("Did you forget to input TreeMap?")
  if contents.find("java.util.Scanner;") == -1:
    raise check50.Failure("Did you forget to input Scanner?")