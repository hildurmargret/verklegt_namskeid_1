def prentButton(bil,merki,ord):
    print "#",
    for _ in range(bil):
        print " ",
    for _ in range(merki):
        print "#",
    for _ in range(bil):
        print " ",
    print "#"

    print "#",
    for _ in range(bil):
        print " ",
    print "#",
    for _ in range(merki-2):
        print " ",
    print "#",
    for _ in range(bil):
        print " ",
    print "#"

    print "#",
    for _ in range(bil):
        print " ",
    print "#",
    print ord+" ",
    print "#",
    for _ in range(bil):
        print " ",
    print "#"

    print "#",
    for _ in range(bil):
        print " ",
    print "#",
    for _ in range(merki-2):
        print " ",
    print "#",
    for _ in range(bil):
        print " ",
    print "#"

    print "#",
    for _ in range(bil):
        print " ",
    for _ in range(merki):
        print "#",
    for _ in range(bil):
        print " ",
    print "#"

def prentSpace(linur,breidd):
    for _ in range(linur):
        print "#",
        for _ in range(breidd-2):
            print " ",
        print "#",


def prentLina(breidd):
    for _ in range(breidd):
        print "#",
    print ""

def prentWord(bil,ord):
    print "#",
    for _ in range(bil):
        print " ",
    print ord,
    for _ in range(bil):
        print " ",
    print "#"
