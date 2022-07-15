def songdict():
    dict = {}
    myfile = open('Power.txt','r')
    lyrics = myfile.readlines()
    for line in lyrics:
        newline = line.split(" ")
        for item in newline:
            item = item.replace(")","").replace("(","").replace("?","").replace("\n","").replace(",","").lower()
            if dict.get(item) is None:
                dict[item] = 1
            else:
                dict[item] += 1
    return dict
    myfile.close()

def staticsong(dict):
    file = open('Power.statistics.txt', 'w')
    for name in dict:
        time = dict.get(name)
        file.write(name + " " + str(time) + "\n")
    file.close()

def program():
    dict = songdict()
    staticsong(dict)

program()