from GEDCOM import GEDCOM
def main():
    filePath = "shakespeare.ged"
    gedcomFile = GEDCOM.fromFile(filePath)
    
    tree = gedcomFile._generateFamilyTree(gedcomFile._individuals[0])
    tree._traverseTree([tree._startNode])

if (__name__ == "__main__"):
    main()