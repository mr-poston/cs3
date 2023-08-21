import check50
import check50.c

def read_tester(line_to_find):
    with open("Tester.java") as file:
        for line in file:
            if line_to_find in line:
                return True
    return False

@check50.check()
def tester_exists():
    """Tester.java exists"""
    check50.c.compile("Tester.java")

@check50.check()
def tester_compiles(tester_exists):
    """Tester.java compiles"""
    check50.run("javac Tester.java")

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