def CompanyDict(filename):
    myfile = open(filename, 'r')
    lines = myfile.readlines()[1:]
    companies = {}

    myfile.close()

    for line in lines:
        Newline = line.split(',')
        SymbolCompany = Newline[0].lower()
        details = (Newline[1].lower(),Newline[2].replace('\n',"").lower())
        companies[SymbolCompany] = details
    return companies

def getCompanys(comDict):
    Companyname = input('Enter Symbol(Stop to stop): ').lower()
    while Companyname != 'stop':
        Comdetails = comDict.get(Companyname)
        if Comdetails is None:
            print(Companyname, 'does not exist')
        else:
            print('Name:',Comdetails[0].capitalize(),"\t","Sector:",Comdetails[1].capitalize())
        Companyname = input('Enter Symbol(stop to stop): ').lower()

def program():
    dict = CompanyDict('companies.csv')
    getCompanys(dict)

program()