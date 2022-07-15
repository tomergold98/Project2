def split(List):
    alist = []
    blist = []
    for num in List:
        if num%2 == 0:
            alist.append(num)
        else:
            blist.append(num)

    return alist,blist

def ex1():
    alist = [1, 3, 4, 6, 7, 9]
    print("List: ", alist)
    Newlist = split(alist)
    print("Odd:",Newlist[1],"Even:",Newlist[0])

ex1()