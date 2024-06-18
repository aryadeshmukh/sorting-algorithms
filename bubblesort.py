
def bubblesort(unsorted_lst, num_iterations = -1):
    '''Sorts unsorted_lst in place using bubblesort.
    
    To test each iteration of bubble sort, set num_iterations to the number of times to go through the array
    while sorting. If num_iterations is less than zero, as it is by default, algorithm will run until
    unsorted_lst is sorted.'''

    return _bubblesort(unsorted_lst, num_iterations)

def _bubblesort(unsorted_lst, num_iterations):
    '''Private function that executes bubblesort.'''

    if (num_iterations == 0):
        return
    
    num_changes = 0

    for i in range(len(unsorted_lst) - 1):
        if compare_and_swap(unsorted_lst, i):
            num_changes += 1
    
    if num_changes > 0:
        return _bubblesort(unsorted_lst, num_iterations - 1)

def compare_and_swap(partially_sorted_lst, i):
    '''Compares value in partially_sorted_lst at index i with value at index i + 1.
    
    If value at index i is greater than value at index i + 1, the two values are swapped in place within
    partially_sorted_lst. If a swap was made, this function returns true. False is returned if no swap
    was made or i >= len(partially_sorted_lst) - 1 or i < 0.'''

    if i < 0 or i >= len(partially_sorted_lst) - 1:
        return False
    
    if partially_sorted_lst[i] > partially_sorted_lst[i + 1]:
        temp = partially_sorted_lst[i + 1]
        partially_sorted_lst[i + 1] = partially_sorted_lst[i]
        partially_sorted_lst[i] = temp
        return True
    
    return False