class Person:
    ID = ""
    name = ""
    sex = ""
    birthDate = ""
    deathDate = ""

    mother = None
    father = None

    def __init__(self, ID, name, sex, birthDate, deathDate):
        self.ID = ID
        self.name = name
        self.sex = sex
        self.birthDate = birthDate
        self.deathDate = deathDate

    def printIndividual(self):
        print("{0}\nb. {1}\nd. {2}\n{3} {4} {5} {6}".format(self.name, self.birthDate, self.deathDate,\
            "Son" if (self.sex == "M") else "Daughter", "of " + self.father.getName() if (self.father is not None) else "Unknown Father",\
            "and", self.mother.getName() if (self.mother is not None) else "Unknown Mother"))

    def getID(self):
        return self.ID

    def getName(self):
        return self.name

    def getMother(self):
        return self.mother

    def getFather(self):
        return self.father

    def getParents(self):
        if (self.mother is None):
            return [self.father]
        if (self.father is None):
            return [self.mother]
        else:
            return [self.father, self.mother]

    def setMother(self, mother):
        self.mother = mother

    def setFather(self, father):
        self.father = father