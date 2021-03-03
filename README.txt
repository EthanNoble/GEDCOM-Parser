INSTRUCTIONS FOR SIMPLE USE
in a Main.py script:
- import GEDCOM from GEDCOM
- call GEDCOM.fromFile("[fileName]") and store the
  return value (a GEDCOM object) in a variable

THINGS YOU CAN DO WITH THE GEDCOM OBJECT
- print the family tree of an individual
  tree = gedcomFile._generateFamilyTree(gedcomFile._individuals[1])
  tree._traverseTree([tree._startNode])

- Search for an individual by name
  individual = gedcomFileObject.searchIndividualById("[PERSON ID]")

- There are more methods you can play with in the GEDCOM class.
  I just wanted to give you a starting place to see what this program
  can do.