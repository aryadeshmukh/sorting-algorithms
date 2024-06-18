from typing import List

def bubblesort(unsorted_lst: List[int]) -> None:
    '''
    Sorts unsorted_lst in place using bubblesort.
    
    Keyword arguments:
    unsorted_lst -- list to be sorted
    '''
    return _bubblesort(unsorted_lst)

def _bubblesort(unsorted_lst: List[int], num_iterations: int = -1) -> None:
    '''
    Sorts unsorted_lst in place using bubblesort.

    Keyword arguments:
    unsorted_lst -- list to be sorted
    num_iterations -- maximum number of times unsorted_lst should be iterated over during bubblesort,
    bubblesort runs to completion if initial value is less than 0 (default -1)
    '''
    while num_iterations != 0:
        num_changes = 0
        for i in range(len(unsorted_lst) - 1):
            if compare_and_swap(unsorted_lst, i):
                num_changes += 1
        if num_changes == 0:
            break
        num_iterations -= 1

def compare_and_swap(partially_sorted_lst: List[int], i: int) -> bool:
    '''
    Compares value at index i with value at index i + 1 in partially_sorted_lst and swaps values in place
    if the two values are not in sorted order. Returns true if a swap was made.

    Keyword arguments:
    partially_sorted_lst -- list to be operated on
    i -- index of value to be compared with next value in partially_sorted_lst
    '''
    if i < 0 or i >= len(partially_sorted_lst) - 1:
        return False
    
    if partially_sorted_lst[i] > partially_sorted_lst[i + 1]:
        temp = partially_sorted_lst[i + 1]
        partially_sorted_lst[i + 1] = partially_sorted_lst[i]
        partially_sorted_lst[i] = temp
        return True
    
    return False