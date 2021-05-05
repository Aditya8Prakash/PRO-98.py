path1 = input('Enter the path of file 1 : ')
path2 = input('Enter the path of file 2 : ')

def swapFileData (p1, p2) :
    file1 = open(p1,'r')
    file2 = open(p2,'r')

    data1 = file1.read()
    data2 = file2.read()

    file1.close()
    file2.close()

    file1 = open(p1,'w')
    file2 = open(p2,'w')

    file1.write(data2)
    file2.write(data1)

    file1.close()
    file2.close()

    print('Data from "'+path1+'" and "'+path2+'" are swapped !')
    exit()

swapFileData(path1, path2)