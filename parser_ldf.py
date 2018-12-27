

def parser():
    f = open('data/hypres.ldf', 'r')
    myList = []
    for line in f:
        myList.append(line)
    print(myList)
    f.close()
    return True
