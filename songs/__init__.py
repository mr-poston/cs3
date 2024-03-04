import check50

def get_contents():
    with open("songs.cpp", "r") as file:
        return file.read()

@check50.check()
def exists():
    """songs.cpp exists"""
    check50.exists("songs.cpp")

@check50.check(exists)
def compiles():
    """songs.cpp compiles"""
    check50.run("make songs").exit(0)

@check50.check(exists)
def test1():
    """Struct contains correct members"""
    contents = get_contents()
    start = contents.index("struct song")
    limit = contents.index("};") + 2
    struct = contents[start:limit]
    if not ("title" in struct and "artist" in struct and "length" in struct):
        raise check50.Failure("The song struct should have 3 members: a `title`, `artist`, and `length` in seconds.")

@check50.check(exists)
def test2():
    """Code creates 2 `song`s and prints their information"""
    contents = get_contents()
    title = contents.count(".title")
    artist = contents.count(".artist")
    length = contents.count(".length")
    if not (title == 4 and artist == 4 and length == 4):
        raise check50.Failure("You need to create and print two `song`s")
    if "cout" not in contents or "printf" not in contents:
        raise check50.Failure("Make sure you print the `song`s to the terminal")

@check50.check(compiles)
def test3():
    """Output is correct"""
    contents = get_contents()
    contents = contents.replace(" ", "")
    lines = contents.split("/n")
    for line in lines:
        if ".title" in line:
            song1_title = line[line.index("=") + 1:line.index(";")]
            song1_title = song1_title.replace('"', '')
        if ".artist" in line:
            song1_artist = line[line.index("=") + 1:line.index(";")]
            song1_artist = song1_title.replace('"', '')
        if ".length" in line:
            song1_length = line[line.index("=") + 1:line.index(";")]
            song1_length = song1_title.replace('"', '')
            break
    for line in lines:
        if ".title" in line:
            song2_title = line[line.index("=") + 1:line.index(";")]
            song2_title = song2_title.replace('"', '')
        if ".artist" in line:
            song2_artist = line[line.index("=") + 1:line.index(";")]
            song2_artist = song2_title.replace('"', '')
        if ".length" in line:
            song2_length = line[line.index("=") + 1:line.index(";")]
            song2_length = song2_title.replace('"', '')
            break
    output = check50.run("./songs").stdout()
    if song1_title not in output:
        raise check50.Failure("Make sure you print the title for the first song")
    if song1_artist not in output:
        raise check50.Failure("Make sure you print the artist for the first song")
    if song1_length not in output:
        raise check50.Failure("Make sure you print the length for the first song")
    if song2_title not in output:
        raise check50.Failure("Make sure you print the title for the second song")
    if song2_artist not in output:
        raise check50.Failure("Make sure you print the artist for the second song")
    if song2_length not in output:
        raise check50.Failure("Make sure you print the length for the second song")

