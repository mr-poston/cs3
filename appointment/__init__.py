import check50

def get_file_lines():
    with open("appointment.cpp", "r") as file:
        content = file.read()
        return content.split("\n")

def get_output_lines():
    output = check50.run("./appointment").stdout()
    return output.split("\n")

@check50.check()
def exists():
    """appointment.cpp exists"""
    check50.exists("appointment.cpp")

@check50.check(exists)
def compiles():
    """appointment.cpp compiles"""
    check50.run("make appointment").exit(0)

@check50.check(exists)
def test1():
    """Function prototype checks out"""
    lines = get_file_lines()
    prototype = False
    for line in lines:
        line = line.replace(" ", "")
        if line.count("string") == 2 and line.count("int") == 2 and "=7" in line and ";" in line:
            prototype = True
            break
    if not prototype:
        sample = "string nextAppointment(string type, int day, int daysToNext = 7);"
        raise check50.Failure("Your prototype should look similar to the following:\n\t" + sample)

@check50.check(exists)
def test2():
    """Function header looks good"""
    lines = get_file_lines()
    header = False
    for line in lines:
        line = line.replace(" ", "")
        if line.count("string") == 2 and line.count("int") == 2 and "=" not in line and ";" not in line:
            header = True
            break
    if not header:
        sample = "string nextAppointment(string type, int day, int daysToNext)"
        raise check50.Failure("Your function header should look similar to the following:\n\t" + sample + "\n\t" + lines)

@check50.check(exists)
def test3():
    """You used a string vector (hopefully to store the days of the week)"""
    lines = get_file_lines()
    vect = False
    for line in lines:
        line = line.replace(" ", "")
        if "vector<string>" in line:
            vect = True
    if not vect:
        raise check50.Failure("You should use a string vector to store the days of the week")

@check50.check(compiles)
def test4():
    check50.run("./appointment").stdin("Oncologist").stdin("3").stdout("Your follow up will be on a Thursday").exit(0)