import check50

@check50.check()
def exists():
    """paper_supplier.cpp exists"""
    check50.exists("paper_supplier.cpp")

@check50.check(exists)
def compiles():
    """paper_supplier.cpp compiles"""
    check50.run("make paper_supplier").exit(0)

@check50.check(compiles)
def test1():
    """Works for input 2200"""
    output = check50.run("./paper_supplier").stdin("2200", prompt=True).stdout()
    lines = output.split("\n")
    if len(lines) != 3:
        raise check50.Failure("Make sure your output is exactly 3 lines (after the user input)")
    dm = 0
    tmspc = 1
    for i in range(len(lines)):
        if "Dunder Mifflin" in lines[i]:
            dm = i
        elif "The Michael Scott Paper Company" in lines[i]:
            tmspc = i
    if "Dunder Mifflin" not in lines[dm] and "9378" not in lines[dm]:
        raise check50.Failure("Output should indicate cost for Dunder Mifflin is 9378")
    if "The Michael Scott Paper Company" not in lines[tmspc] and "8998" not in lines[tmspc]:
        raise check50.Failure("Output should indicate cost for The Michael Scott Paper Company is 8998")
    if "The Michael Scott Paper Company" not in lines[2]:
        raise check50.Failure("Output should suggest switching to The Michael Scott Paper Company")

@check50.check(compiles)
def test2():
    """Works for input 3500"""
    output = check50.run("./paper_supplier").stdin("3500", prompt=True).stdout()
    lines = output.split("\n")
    if len(lines) != 3:
        raise check50.Failure("Make sure your output is exactly 3 lines (after the user input)")
    dm = 0
    tmspc = 1
    for i in range(len(lines)):
        if "Dunder Mifflin" in lines[i]:
            dm = i
        elif "The Michael Scott Paper Company" in lines[i]:
            tmspc = i
    if "Dunder Mifflin" not in lines[dm] and "14165" not in lines[dm]:
        raise check50.Failure("Output should indicate cost for Dunder Mifflin is 14165")
    if "The Michael Scott Paper Company" not in lines[tmspc] and "14315" not in lines[tmspc]:
        raise check50.Failure("Output should indicate cost for The Michael Scott Paper Company is 14315")
    if "The Michael Scott Paper Company" not in lines[2]:
        raise check50.Failure("Output should suggest staying with Dunder Mifflin")