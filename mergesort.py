
def mergesort(lst):
    '''Uses mergesort to sort input list.'''

    if (len(lst) <= 1):
        return lst

    left = lst[:len(lst) // 2]
    right = lst[len(lst) // 2:]
    sorted_left = mergesort(left)
    sorted_right = mergesort(right)

    return merge(sorted_left, sorted_right)

def merge(lst1, lst2):
    '''Helper function for mergesort.
    
    Returns a new sorted list containing all elements of two sorted input lists.'''

    merged_list = []
    i = 0
    j = 0

    while i < len(lst1) or j < len(lst2):
        if i < len(lst1) and j < len(lst2):
            if lst1[i] < lst2[j]:
                merged_list.append(lst1[i])
                i += 1
            else:
                merged_list.append(lst2[j])
                j += 1
        elif i < len(lst1):
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1
    
    return merged_list
