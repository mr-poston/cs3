import check50

@check50.check()
def exists1():
    """Part.java exists"""
    check50.exists("Part.java")

@check50.check()
def exists2():
    """PartList.java exists"""
    check50.exists("PartList.java")

@check50.check()
def compiles1():
    """Part.java compiles"""
    check50.run("javac Part.java").exit(0)

@check50.check()
def compiles2():
    """PartList.java compiles"""
    check50.run("javac PartList.java").exit(0)

@check50.check(compiles1, compiles2)
def file_check():
    """Reads from autoparts.dat correctly"""
    output = check50.run("java PartList").stdout()

    lines = ["Chevy Camaro 2002 Wiper Blades 12321 - 1",
             "Chevy Silverado 2002 Air Filter 98765 - 2",
             "Dodge Dakota 2001 Radiator 23102 - 1",
             "Ford Expedition 1997 Water Pump 19912 - 1",
             "Ford Taurus 1999 Fuel Filter 19967 - 1",
             "Ford Taurus 1999 Water Pump 19934 - 2"]
    for line in enumerate(lines):
        if line[1] not in output:
            raise check50.Failure("Output should be:\nChevy Camaro 2002 Wiper Blades 12321 - 1\nChevy Silverado 2002 Air Filter 98765 - 2\nDodge Dakota 2001 Radiator 23102 - 1\nFord Expedition 1997 Water Pump 19912 - 1\nFord Taurus 1999 Fuel Filter 19967 - 1\nFord Taurus 1999 Water Pump 19934 - 2\n")

@check50.check(compiles1, compiles2)
def test0():
    """Part.java constructor works"""
    check50.run("java Checker part constructor").stdout("Chrystler Pacifica 2019 Radiator 74219", regex=False).exit(0)

@check50.check(compiles1, compiles2)
def test1():
    """Part.java compareTo works for different makes"""
    check50.run("java Checker part compare1").stdout("-1", regex=False).exit(0)

@check50.check(compiles1, compiles2)
def test2():
    """Part.java compareTo works for different models"""
    check50.run("java Checker part compare2").stdout("29", regex=False).exit(0)

@check50.check(compiles1, compiles2)
def test3():
    """Part.java compareTo works for different years"""
    check50.run("java Checker part compare3").stdout("-1", regex=False).exit(0)

@check50.check(compiles1, compiles2)
def test4():
    """Part.java compareTo works for different part name"""
    check50.run("java Checker part compare4").stdout("12", regex=False).exit(0)

@check50.check(compiles1, compiles2)
def test5():
    """PartList.java no-parameter constructor works"""
    check50.run("java Checker list empty").stdout("", regex=False).exit(0)

@check50.check(compiles1, compiles2)
def test6():
    """PartList.java putEntry works for 1 instance of a part"""
    check50.run("java Checker list putEntry1").stdout("Ford Taurus 1999 Water Pump 19934 - 1", regex=False).exit(0)

@check50.check(compiles1, compiles2)
def test7():
    """PartList.java putEntry works for multiple instances of a part"""
    check50.run("java Checker list putEntry1").stdout("Ford Taurus 1999 Water Pump 19934 - 2", regex=False).exit(0)