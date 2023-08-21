import check50

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
def player_exists():
    """Player.java exists"""
    check50.exists("Player.java")

@check50.check()
def import_scanner(tester_exists):
    """import Scanner"""
    if not read_tester("import java.util."):
        raise check50.Failure("Did you import java.util.Scanner?")
    if not read_tester("Scanner") or not read_tester("*"):
        raise check50.Failure("Did you import java.util.Scanner?")
