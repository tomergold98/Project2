NameClass = 'Management Information Systems'

def printStudentsData(lst,class_):
    print(class_ + ':')
    for item in lst:
        if item[2] == class_:
            print(item)

def ex3():
    acc1 = (123456,'Moshe Zuchmir','Management Information Systems')
    acc2 = (246810,'Daphna Ketshup','Nutrition')
    acc3 = (135793,'James Bond','Business Administration')
    acc4 = (987654,'Harry Potter','Management Information Systems')
    Students = [acc1,acc2,acc3,acc4]
    printStudentsData(Students,NameClass)

ex3()


