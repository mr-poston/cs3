import check50

@check50.check()
def exists():
    """Acronyms.java exists"""
    check50.exists("Acronyms.java")

@check50.check()
def compiles():
    """Acronyms.java compiles"""
    check50.run("javac Acronyms.java").exit(0);

@check50.check()
def file_check():
    """Reads from acronyms.dat correctly"""
    output = check50.run("java Acronyms").stdout()

    if "{CPU=Central Processing Unit" not in output or "TSO=Texas State Optical}" not in output:
        raise check50.Failure("Did you forget to print the map contents?")
    check50.run("java Acronyms").stdout("I drove my Pick Up to Texas State Optical to get a Hard Drive\. My.*\\nCentral Processing Unit has a virus\. I sometimes Strike Out.*\\nwhen trying to kick a Field Goal\. I had 2 Runs Batted In.*\\nat the game\..*", regex=True).exit(0)

@check50.check()
def test_0_contructor():
    """No parameter constructor works"""
    check50.run("java Checker Constructor").stdout("{}", regex=False).exit(0)

@check50.check()
def test_put_entry():
    """putEntry method works"""
    check50.run("java Checker putEntry").stdout("{RHS=Richardson High School}", regex=False).exit(0)

@check50.check()
def test_convert1():
    """convert method works with punctuation after acronym"""
    check50.run("java Checker convert1").stdout("I go to Richardson High School\..*", regex=True).exit(0)

@check50.check()
def test_convert2():
    """convert method works with no punctuation"""
    check50.run("java Checker convert2").stdout("Richardson High School is cool\..*", regex=True).exit(0)

@check50.check(exists)
def imports():
  """Import statements"""
  f = open("Relatives.java", "r")
  contents = f.read()
  if contents.find("util.*") != -1:
    raise check50.Failure("Import each class separately!!")
  if contents.find("io.*") != -1:
    raise check50.Failure("Import each class separately!!")