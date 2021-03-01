from Containers import Individual
from Containers import Family
from Containers import Date
class Parser:
    individuals = []
    families = []

    def __init__(self, fileName):
        self._parseIndividuals(fileName)
        self._parseFamilies(fileName)
    
    def _parseDate(self, line):
        if ("DATE" in line):
            return Date(line.split(" DATE ")[1].replace("\n", ""))

    def _parseIndividuals(self, fileName):
        file = open(fileName, "r")
        breakLoop = False
        while (not breakLoop):
            fileLine = file.readline()
            #Find where an individual's information starts
            if ("INDI" in fileLine):
                indID = fileLine.split("@")[1]
                famcID = None
                famsID = None
                name = None
                sex = None
                birth = None
                death = None
                while (True):
                    lastPosition = file.tell()
                    fileLine = file.readline()
                    #Parse out the famc and fams ID
                    if ("1 FAMC" in fileLine):
                        famcID = fileLine.split("@")[1]
                    if ("1 FAMS" in fileLine):
                        famsID = fileLine.split("@")[1]
                    #Parse out the name if the line contains a name
                    if ("1 NAME" in fileLine):
                        name = fileLine[7:len(fileLine) - 1].replace("/", "").replace("\n", "")
                    #Parse out the sex if the line contains a gender
                    if ("1 SEX" in fileLine):
                        sex = fileLine[6]
                    #Parse out the birth and death date if the line contains such
                    if ("1 BIRT" in fileLine):
                        fileLine = file.readline()
                        birth = self._parseDate(fileLine)
                    if ("1 DEAT" in fileLine):
                        fileLine = file.readline()
                        death = self._parseDate(fileLine)
                    #If the next individual in the file is found, end the inner loop
                    #and go back to the previous line in the file. This is done to prevent
                    #the algorithm from skipping the first line of an individuals information
                    if ("INDI" in fileLine):
                        file.seek(lastPosition)
                        self.individuals.append(Individual(indID, famcID, famsID, name, sex, birth, death))
                        break
                    #End the inner and outer loop if the end of the file has been reached
                    if ("0 TRLR" in fileLine):
                        self.individuals.append(Individual(indID, famcID, famsID, name, sex, birth, death))
                        breakLoop = True
                        break
        file.close()
    
    def _parseFamilies(self, fileName):
        file = open(fileName, "r")
        breakLoop = False
        while (not breakLoop):
            fileLine = file.readline()
            #Find where an individual's information starts
            if ("FAM" in fileLine and "FAMC" not in fileLine and "FAMS" not in fileLine):
                famID = fileLine.split("@")[1]
                husband = None
                wife = None
                marriageDate = None
                children = []
                while (True):
                    lastPosition = file.tell()
                    fileLine = file.readline()
                    #Parse out the husband
                    if ("1 HUSB" in fileLine):
                        husband = fileLine.split("@")[1]
                    #Parse out the wife
                    if ("1 WIFE" in fileLine):
                        wife = fileLine.split("@")[1]
                    #Parse out the marriage date
                    if ("1 MARR" in fileLine):
                        fileLine = file.readline()
                        marriageDate = self._parseDate(fileLine)
                    #Parse out the children
                    if ("1 CHIL" in fileLine):
                        children.append(fileLine.split("@")[1])
                    if ("FAM" in fileLine and "FAMC" not in fileLine and "FAMS" not in fileLine):
                        file.seek(lastPosition)
                        self.families.append(Family(famID, husband, wife, marriageDate, children))
                        break
                    #End the inner and outer loop if the end of the file has been reached
                    if ("0 TRLR" in fileLine):
                        self.families.append(Family(famID, husband, wife, marriageDate, children))
                        breakLoop = True
                        break
        file.close()