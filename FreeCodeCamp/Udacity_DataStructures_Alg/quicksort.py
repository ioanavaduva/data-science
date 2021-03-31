"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):

    if len(array) <= 1:
        return array

    piv_index = len(array) -1 
    pivot = array[piv_index]
    i = 0
    j = 0
    
    while i < len(array) - 1:
        if pivot <= array[j]:
            array.insert(piv_index, array.pop(j))
            piv_index = array.index(pivot)            
            if j != piv_index:
                array.insert(j, array.pop(piv_index-1))             
        else:
            j = j + 1

        i = i +1
        
    array[0:piv_index] = quicksort(array[0:piv_index]) 
    array[piv_index + 1:] = quicksort(array[piv_index + 1:])

    return array

short_test = [8, 3, 1, 7, 0, 10, 2]
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test)) #[7, 3, 10, 8]