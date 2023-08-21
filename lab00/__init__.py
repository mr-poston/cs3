import check50

output = ""

def get_output(file_to_run):
    return check50.run("java " + file_to_run).stdout()

def read_tester(line_to_find):
    with open("Tester.java") as file:
        for line in file:
            if line_to_find in line:
                return True
    return False

@check50.check()
def tester_exists():
    """Tester.java exists"""
    check50.exists("Tester.java")

@check50.check()
def tester_compiles(tester_exists):
    """Tester.java compiles"""
    check50.run("javac Tester.java")

@check50.check()
def print_hello(tester_exists):
    """Prints 'Hello again, world!'"""
    expected = "[Hh]ello again, [Ww]orld!"
    actual = get_output("Tester")
    if expected not in actual:
        raise check50.Failuer("Output must print 'Hello again, world!'")

@check50.check()
def import_scanner(tester_exists):
    """import Scanner"""
    if not read_tester("import java.util."):
        raise check50.Failure("Did you import java.util.Scanner?")
    if not (read_tester(".Scanner") or read_tester(".*")):
        raise check50.Failure("Did you import java.util.Scanner?")

@check50.check()
def player_exists():
    """Player.java exists"""
    check50.exists("Player.java")

@check50.check()
def player_compiles(player_exists):
    """Player.java compiles"""
    check50.run("javac Player.java")