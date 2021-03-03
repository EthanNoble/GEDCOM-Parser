INSTRUCTIONS FOR SIMPLE USE
in a Main.py script:
- import GEDCOM from GEDCOM
- call GEDCOM.fromFile("[fileName]") and store the
  return value (a GEDCOM object) in a variable

THINGS YOU CAN DO WITH THE GEDCOM OBJECT
- print the family tree of an individual back by 5 generations
  tree = gedcomFile._generateFamilyTree(gedcomFile._individuals[50], 5)
    for g in range(0, len(tree._treeList)):
        for p in range(0, len(tree._treeList[g])):
            print(tree._treeList[g][p]._name)
        print("---------------------")

- Search for an individual by ID
  individual = gedcomFileObject.searchIndividualById("[PERSON ID]")

- There are more methods you can play with in the GEDCOM, Individual, Date, and Family classes.
  I just wanted to give you a starting place to see what this program
  can do.