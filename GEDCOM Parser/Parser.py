from Person import Person

class Parser:
    gedcomFile = ""
    individualsWithData = []

    def __init__(self, gedcomFile):
        self.gedcomFile = gedcomFile
        self.initializeParser()

    def findIndividuals(self, content):
        individuals = []
        for i in range(0, len(content)):
            if ("INDI" in content[i]):
                startOfRecordIndex = i
                i += 1
                individual = []
                while (content[i][0] != "0"):
                    individual.append(content[i])
                    i += 1
                individuals.append(individual)
                i = startOfRecordIndex
        return individuals

    def getIndividualName(self, individual):
        name = ""
        for line in individual:
            if ("NAME" in line):
                name = line[7:line.index("\n")]
        if ("/" in name):
            nameList = []
            for i in range(0, len(name)):
                if (name[i] != "/"):
                    nameList.append(name[i])
            name = "".join(nameList)
        return name

    def getIndividualBirthDate(self, individual):
        birthDate = ""
        for i in range(0, len(individual)):
            if ("BIRT" in individual[i]):
                i += 1
                birthDate = individual[i][7:individual[i].index("\n")]
        return birthDate

    def getIndividualDeathDate(self, individual):
        deathDate = ""
        for i in range(0, len(individual)):
            if ("DEAT" in individual[i]):
                i += 1
                deathDate = individual[i][7:individual[i].index("\n")]
        return deathDate

    def getIndividualSex(self, individual):
        sex = ""
        for i in range(0, len(individual)):
            if ("SEX" in individual[i]):
                sex = individual[i][6]
        return sex

    def findFamilies(self, content):
        families = []
        for i in range(0, len(content)):
            if ("FAM" in content[i] and content[i][0] == "0"):
                startOfRecordIndex = i
                i += 1
                family = []
                while (content[i][0] != "0"):
                    family.append(content[i])
                    i += 1
                families.append(family)
                i = startOfRecordIndex
        return families

    def searchForIndividualByName(self, name):
        for individual in self.individualsWithData:
            if (individual.getName() == name):
                return individual

    def searchForIndividualById(self, ID):
        for individual in self.individualsWithData:
            if (individual.getID() == ID):
                return individual

    def constructFamilies(self, families):
        for i in range(0, len(families)):
            for v in range(0, len(families[i])):
                father = None
                mother = None
                if ("CHIL" in families[i][v]):
                    childID = families[i][v][7:families[i][v].index("\n")]
                    child = self.searchForIndividualById(childID)
                    for j in range(0, len(families[i])):
                        if ("HUSB" in families[i][j]):
                            fatherID = families[i][j][7:families[i][j].index("\n")]
                            father = self.searchForIndividualById(fatherID)
                            child.setFather(father)
                        if ("WIFE" in families[i][j]):
                            motherID = families[i][j][7:families[i][j].index("\n")]
                            mother = self.searchForIndividualById(motherID)
                            child.setMother(mother)

    def printFamilyTree(self, startIndividual, generations, currentGeneration=1):
        print("Generation {0}\n-------------------------".format(currentGeneration + 1))
        parents = []
        for name in startIndividual:
            individual = self.searchForIndividualByName(name)
            if (individual is not None):
                for parent in individual.getParents():
                    parents.append(parent)
        for parent in parents:
            if (parent is not None):
                parent.printIndividual()
                print("")
        for i in range(0, len(parents)):
            if (parents[i] is not None):
                parents[i] = parents[i].getName()
        if (currentGeneration < generations):
            self.printFamilyTree(parents, generations, currentGeneration + 1)

    def initializeParser(self):
        fileContent = []
        with open(self.gedcomFile, "r") as file:
            line = file.readline()
            while (line != ""):
                fileContent.append(line)
                line = file.readline()
        individuals = self.findIndividuals(fileContent)
        families = self.findFamilies(fileContent)

        names = []
        for i in range(0, len(individuals)):
            name = self.getIndividualName(individuals[i])
            names.append(name)
        birthDates = []
        for i in range(0, len(individuals)):
            birthDate = self.getIndividualBirthDate(individuals[i])
            birthDates.append(birthDate)
        deathDates = []
        for i in range(0, len(individuals)):
            deathDate = self.getIndividualDeathDate(individuals[i])
            deathDates.append(deathDate)
        sexes = []
        for i in range(0, len(individuals)):
            sex = self.getIndividualSex(individuals[i])
            sexes.append(sex)
        IDS = []
        for i in range(1, len(individuals)+1):
            IDS.append("@P{0}@".format(i))

        for i in range(0, len(individuals)):
            self.individualsWithData.append(Person(IDS[i], names[i], sexes[i], birthDates[i], deathDates[i]))

        self.constructFamilies(families)