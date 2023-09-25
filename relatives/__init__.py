import check50
import re

@check50.check()
def exists():
    """Relatives.java exists"""
    check50.exists("Relatives.java")

@check50.check()
def compiles():
    """Relatives.java compiles"""
    check50.run("javac Relatives.java").exit(0);

@check50.check()
def file_check():
    """Reads from relatives.data correctly"""
    output = check50.run("java Relatives").stdout()
    expected1 = "Almas.*Brian.*\\nBob.*John Tom.*\\nDot.*Chuck Fred Jason Tom.*\\nElton.*Linh.*\\nFred.*Alice James.*\\nJim.*Sally Tammy Tom.*\\nTimmy.*Amanda.*\\n\\n.*"
    expected2 = ".*Dot.*\[Chuck, Fred, Jason, Tom\]\n"

    if not re.match(expected1, output):
        raise check50.Failure("Did you forget to print each person's relatives in your main method?")
    if not re.match(expected2, output):
        raise check50.Failure("Did you forget to read the last name from the file and print their relatives?")
    check50.run("java Relatives").exit(0)

@check50.check()
def test_0_contructor():
    """No parameter constructor works"""
    check50.run("java Checker Constructor").stdout("", regex=False).exit(0)

@check50.check()
def test_set_sentence():
    """putEntry method works"""
    check50.run("java Checker setPersonRelative").stdout("Almas is related to Bob Brian \nDot is related to Fred \n", regex=False).exit(0)

@check50.check()
def test_set_sentence():
    """putEntry method works"""
    check50.run("java Checker getRelatives").stdout("[Chuck, Fred, Jason, Tom]", regex=False).exit(0)

@check50.check(exists)
def imports():
  """Import statements"""
  f = open("Relatives.java", "r")
  contents = f.read()
  if contents.find("util.*") != -1:
    raise check50.Failure("Import each class separately!!")
  if contents.find("io.*") != -1:
    raise check50.Failure("Import each class separately!!")