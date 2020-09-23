from Parser import Parser

def main():
    GEDCOM = Parser("shakespeare.ged")
    print(GEDCOM.individualsWithData[0].sex)

if __name__ == "__main__":
    main()