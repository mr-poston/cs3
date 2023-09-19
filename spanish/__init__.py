import check50

@check50.check()
def exists():
    """SpanToEng.java exists"""
    check50.exists("SpanToEng.java")

@check50.check()
def compiles():
    """SpanToEng.java compiles"""
    check50.run("javac SpanToEng.java").exit(0);

@check50.check()
def file_check():
    """Reads from spantoeng.data correctly"""
    check50.run("java SpanToEng").exit(0)
    output = check50.run("java SpanToEng").stdout()
    if "{a=to" not in output and "yo=i}" not in output:
        raise check50.Failure("Did you forget to print the map contents?")
    if "my hair is brown" not in output:
        raise check50.Failure("Did you forget to print the translated sentences?")

@check50.check()
def test_put_entry():
    """putEntry method works"""
    check50.run("java Checker 1").stdout("{ordenador=computer\n quiero=want\n una=a\n virus=virus\n yo=i}").exit(0)

@check50.check()
def test_translate():
    """translate method works"""
    check50.run("java Checker 2").stdout("i want a computer virus").exit(0)

@check50.check(exists)
def imports():
  """Import statements"""
  f = open("SpanToEng.java", "r")
  contents = f.read()
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
  if contents.find("util.*") != -1:
    raise check50.Failure("Import each class separately!!")
  if contents.find("io.*") != -1:
    raise check50.Failure("Import each class separately!!")