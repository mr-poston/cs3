import check50

def get_file_lines(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content.split("\n")

@check50.check()
def exists():
    """patient.cpp exists"""
    check50.exists("patient.cpp")

@check50.check()
def util_exists():
    """util.cpp and util.h exist"""
    check50.exists("util.cpp")
    check50.exists("util.h")

@check50.check(exists)
def compiles():
    """code compiles"""
    check50.run("make patient").exit(0)

@check50.check()
def test1():
    check50.run("./patient").stdin("David").stdin("98.7") \
                            .stdin("Louise").stdin("99.9") \
                            .stdin("Walter").stdin("90").stdin("108").stdin("97") \
                            .stdin("Jacob").stdin("100.5").stdin("exit") \
                            .stdout(".*DAVID\nLOUISE\nWALTER").exit(0)