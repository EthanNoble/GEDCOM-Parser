from Parser import Parser
import DataStructures
class GEDCOM:
    _individuals = []
    _families = []
    
    def __init__(self, individuals, families):
        self._individuals = individuals
        self._families = families
        self._setIDMembersToObjects()
    
    def _generateFamilyTree(self, startIndividual, generations):
        parentOne = self.searchFamilyById(startIndividual._famcID)
        if (parentOne != None):
            parentOne = DataStructures.Node(parentOne._husband)
        parentTwo = self.searchFamilyById(startIndividual._famcID)
        if (parentTwo != None):
            parentTwo = DataStructures.Node(parentTwo._wife)
        firstIndividual = DataStructures.Node(startIndividual, None, parentOne, parentTwo)
        return DataStructures.Tree(firstIndividual, self._families, generations)

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