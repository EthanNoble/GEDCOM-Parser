class Family:
    ID = ""
    husband = None
    wife = None
    children = []
    marriageDate = ""
    marriagePlace = ""

    def __init__(self, ID, husband, wife, children, marriageDate, marriagePlace):
        self.ID = ID
        self.husband = husband
        self.wife = wife
        self.children = children
        self.marriageDate = marriageDate
        self.marriagePlace = marriagePlace

    def printFamily(self):
        print("Family - {0}\n\tHusband: {1}\n\tWife: {2}\n".format(self.ID, "Unknown Father" if (self.husband == None) else self.husband.name, "Unkown Mother" if (self.wife == None) else self.wife.name))
        print("\tMarriage: {0} in {1}\n".format(self.marriageDate, self.marriagePlace))
        print("\tChildren - ")
        for child in self.children:
            print("\t    " + child.name)
        print("\n")

    def printIndividual(self):
        pass