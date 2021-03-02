from GEDCOM import GEDCOM
def main():
    filePath = ""
    gedcomFile = GEDCOM.fromFile(filePath)

    tree = gedcomFile._generateFamilyTree(gedcomFile._individuals[1])
    tree._traverseTree([tree._startNode])

if (__name__ == "__main__"):
    main()