def getCelebrities():
    dict = {}
    for i in range(2):
        Name = input('Enter celebrity name: ')
        Income = int(input('Enter '+Name+'\'s income: '))
        dict[Name.lower()] = Income
    return dict

def getCelebIncome(celebDict):
    query = input('Query celebrity name(none to exit): ').lower()
    while query != 'none':
        price = celebDict.get(query)
        if price is None:
            print(query, 'does not exist')
        else:
            print('Income:',price)
        query = input('Query celebrity name(none to exit): ').lower()

def ex2():
    celebDict = getCelebrities()
    getCelebIncome(celebDict)

ex2()
