import time
# Python program for implementation of heap Sort 
#num = int(raw_input("How many numbers to sort? "))
  
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 

    n = len(arr) 
      
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
      
        # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
  
# Driver code to test above 
#arr = [ 12, 11, 13, 5, 6, 7] 
#heapSort(arr) 
#n = len(arr) 
#print ("Sorted array is") 
#for i in range(n): 
 #   print ("%d" %arr[i]), 


with open(raw_input("Please input test file path: ")) as infile:
    for i, line in enumerate(infile):
        field = map(int, line.split(" "))

        timeStart = time.clock()
        heapSort(field)
        #mergeSort(field, 0, num-1)
        timeEnd = time.clock()

        timeTot = timeEnd - timeStart

        print ("\nSorted array is")
        for i in range(15000):
            print ("%d" %
            field[i])
        print '\n\nTime elapsed: ', timeTot, 'seconds'