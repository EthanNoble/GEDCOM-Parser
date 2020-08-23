INSTRUCTIONS FOR SIMPLE USE (Ancestry.com gedcom file recommended for best performance)
In a main .py script:
- import Parser from Parser
- Create a Parser object, passing the path of the GEDCOM file into the constructor

THINGS YOU CAN DO WITH THE PARSER OBJECT
- Print the family tree of an individual.
  gedcomObject.printFamilyTree(["John Doe"], 5)

- Search for an individual by name.
  gedcomObject.searchForIndividualByName("John Doe")
  Returns the individual's object of class Person. You can access
  attributes of the object, ex. getName(), getParents() etc..

- There are more methods you can play with in the Parser class.
  I just wanted to give you starting place to see what this program
  can do.

THINGS YOU CAN DO WITH A PERSON OBJECT
- Call the printIndividual method of a Person object to
  print out a small biography of the person containing
  name, DOB/DOD, and parents.

THINGS YOU CAN DO WITH A FAMILY OBJECT
- To get a family object of an individual (an individual can belong to
  multiple families), you can use the following code:

  for family in gedcomObject.searchForFamilyByIndividualName(INDIVIDUAL_NAME):
        print(family.printFamily())
  

This is a very rudimentary and early version of this project. I just wanted to see how far I could get in building this and it turned out fairly decent.
I will probably work on this alot more as there are many other features I want to add.

CONTACT
ethan.noble@noblefamilytree.com