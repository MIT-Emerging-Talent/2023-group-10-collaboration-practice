def quick_sort(listToSort):
    '''
    The quick_sort function takes an array that we should to sort and calls a next function with the such parameters:
    
    -listSort - the array we should sort
    -low - 0(serial number of the first element)
    -high - serial number of the last element in array
    
    return: 
    - arraySorted - sorted array
    '''
    arraySorted = helperFunction(listToSort, 0, len(listToSort)-1)
    return arraySorted

def helperFunction(listSort, low, high):
    '''
    Recursively perform the main work of the quicksort algorithm to sort a list.

    This function partitions the list and recursively applies the quicksort algorithm
    to the sublists on both sides of the pivot until the entire list is sorted.

    Parameters:
    - listSort (list): The list to be sorted.
    - low (int): The starting index of the sublist to be sorted.
    - high (int): The ending index of the sublist to be sorted.

    Returns:
    listSort: The sorted list after applying the quicksort algorithm.
    '''
    if low<high:
        j = partition(listSort, low, high)
        helperFunction(listSort, low, j)
        helperFunction(listSort, j+1, high)
    return listSort
        
        
def partition(listSort, low, high):
    '''
    Partition the given list in-place based on a pivot element.
    
    Parameters:
    - listSort (list): The list to be partitioned.
    - low (int): The starting index of the partition within the list.
    - high (int): The ending index of the partition within the list.
    
    Returns:
    int: The index of the pivot element after partitioning. All elements to the left
         of this index are less than or equal to the pivot, and all elements to the
         right are greater than the pivot.
    '''
    pivot = listSort[low]
    i=low+1
    j=high
    while True:
        while i <= j and listSort[i] <= pivot:
            i = i + 1
        while i <= j and listSort[j] > pivot:
            j = j - 1
        if i <= j:
            listSort[i], listSort[j] = listSort[j], listSort[i]
        else:
            break
    listSort[low], listSort[j]=listSort[j], listSort[low]
    return j 
print(quick_sort([5,4,3,2,1]))  
    
            
        
    
    
    