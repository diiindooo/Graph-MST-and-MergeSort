import time
num = int(raw_input("How many numbers to sort? "))


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) / 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

def bubbleSort():
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

#alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(passnum)
print(passnum)


with open(raw_input("Please input test file path: ")) as infile:
    for i, line in enumerate(infile):
        field = map(int, line.split(" "))

        timeStart = time.clock()
        mergeSort(field, 0, num-1)
        timeEnd = time.clock()

        timeTot = timeEnd - timeStart

        print ("\nSorted array is")
        for i in range(num):
            print ("%d" %
            field[i])
        print '\n\nTime elapsed: ', timeTot, 'seconds'


