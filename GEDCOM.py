from Parser import Parser
from DateStructures import Node
from DateStructures import Tree
class GEDCOM:
    _individuals = []
    _families = []
    _treeObject = None
    
    def __init__(self, individuals, families):
        self._individuals = individuals
        self._families = families
        self._setIDMembersToObjects()
        self._generateFamilyTree()
    
    def _generateFamilyTree(self):
        parentOne = self.searchFamilyById(self._individuals[0]._famcID)
        if (parentOne != None):
            parentOne = Node(parentOne._husband)
        parentTwo = self.searchFamilyById(self._individuals[0]._famcID)
        if (parentTwo != None):
            parentTwo = Node(parentTwo._wife)
        firstIndividual = Node(self._individuals[0], None, parentOne, parentTwo)
        self._treeObject = Tree(firstIndividual, self._families)

    @staticmethod
    def fromFile(fileName):
        parser = Parser(fileName)
        return GEDCOM(parser.individuals, parser.families)

    def _setIDMembersToObjects(self):
        for i in range(0, len(self._families)):
            husbandID = self._families[i]._husband
            wifeID = self._families[i]._wife
            self._families[i]._husband = self.searchIndividualById(husbandID)
            self._families[i]._wife = self.searchIndividualById(wifeID)
            for v in range(0, len(self._families[i]._children)):
                childID = self._families[i]._children[v]
                self._families[i]._children[v] = self.searchIndividualById(childID)
                

    def searchIndividualById(self, id):
        for individual in self._individuals:
            if (individual._indID == id):
                return individual
        return None
    
    def searchFamilyById(self, id):
        for family in self._families:
            if (family._famID == id):
                return family
        return None
    
    def displayIndividuals(self):
        for i in range(0, len(self._individuals)):
            self._individuals[i].display()
    
    def displayFamilies(self):
        for i in range(0, len(self._families)):
            self._families[i].display()

def searchFamilyByIdStatic(id, families):
        for family in families:
            if (family._famID == id):
                return family
        return None