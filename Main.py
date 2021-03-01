from GEDCOM import GEDCOM
def main():
    filePath = ""
    gedcomFile = GEDCOM.fromFile(filePath)
    gedcomFile._treeObject._traverseTree(gedcomFile._families, [gedcomFile._treeObject._startNode])

if (__name__ == "__main__"):
    main()