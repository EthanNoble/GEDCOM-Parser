class Individual:
    _indID = None
    _famcID = None
    _famsID = None
    _name = None
    _sex = None
    _birth = None
    _death = None

    def __init__(self, indID, famcID, famsID, name, sex, birth, death):
        self._indID = indID
        self._famcID = famcID
        self._famsID = famsID
        self._name = name
        self._sex = sex
        self._birth = birth
        self._death = death
    
    def display(self):
        print(self._indID)
        print(self._famcID)
        print(self._famsID)
        print(self._name)
        print(self._sex)
        if (self._birth != None):
            print(self._birth.display())
        else:
            print("Unknown")
        if (self._death != None):
            print(self._death.display(), "\n")
        else:
            print("Unknown\n")

class Family:
    _famID = None
    _husband = None
    _wife = None
    _marriageDate = None
    _children = []

    def __init__(self, famID, husband, wife, marriageDate, children):
        self._famID = famID
        self._husband = husband
        self._wife = wife
        self._marriageDate = marriageDate
        self._children = children
    
    def display(self):
        print(self._famID)
        if (self._husband != None):
            print(self._husband._name)
        else:
            print("Unknown husband")
        if (self._wife != None):
            print(self._wife._name)
        else:
            print("Unknown wife")
        if (self._marriageDate != None):
            self._marriageDate.display()
        else:
            print("Unknown marriage date")
        for child in self._children:
            print(child._name)
        print("\n")

class Date:
    _day = None
    _month = None
    _year = None
    _failedToParse = False

    def __init__(self, date):
        self._parseDate(date)

    @staticmethod
    def _getIntegerMonth(month):
        months1 = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        months2 = ["Jan", "Feb", "Mar", "Apr", "Ma", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
        months3 = ["Ja", "Fe", "Ma", "Ap", "M", "Ju", "J", "Au", "Sep", "Oc", "No", "De"]
        for i in range(0, 12):
            if (months1[i].lower() == month.lower() or
            months2[i].lower() == month.lower() or
            months3[i].lower() == month.lower()):
                return i + 1
    
    def _parseDate(self, date):
        dateList = date.split(" ")
        if (len(dateList) == 1):
            self._year = dateList[0]
        elif (len(dateList) == 2):
            self._month = self._getIntegerMonth(dateList[0])
            self._year = dateList[1]
        elif (len(dateList) == 3):
            self._day = dateList[0]
            self._month = self._getIntegerMonth(dateList[1])
            self._year = dateList[2]
        else:
            self._failedToParse = True

    def display(self):
        if (self._failedToParse):
            print("Failed to parse date")
        else:
            print(self._day, " ", self._month, " ", self._year)