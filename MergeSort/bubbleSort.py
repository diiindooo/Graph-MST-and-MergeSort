import sys
print "Enter number of numbers"
n = int(raw_input().strip())
with open(raw_input("Please input test file path: ")) as infile:
    for i, line in enumerate(infile):
        a = map(int, line.split(" "))
i = n
numberOfSwaps = 0
def bubbleSort(n, 1, r):
    for i in xrange(n, 0, -1):
        for j in range(0,i-1):
            #print a[j]
            if a[j]>a[j+1]:
                temp = a[j] 
                a[j] = a[j+1]
                a[j+1] = temp
                numberOfSwaps =numberOfSwaps+1 ;
        i = i-1    
    print "Sorted array :"
