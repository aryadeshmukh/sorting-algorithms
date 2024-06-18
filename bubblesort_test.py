from bubblesort import bubblesort
from bubblesort import compare_and_swap

def test_compare_and_swap():
    '''Tests the compare_and_swap function from bubblesort.'''

    test_list_1 = [1, 5, 4, 6]
    test_index_1 = 1
    assert compare_and_swap(test_list_1, test_index_1)
    assert test_list_1 == [1, 4, 5, 6], test_list_1

    test_list_2 = [1, 2, 3]
    test_index_2 = 0
    assert not compare_and_swap(test_list_2, test_index_2)
    assert test_list_2 == [1, 2, 3], test_list_2

    test_list_3 = [1, 3, 7, 6, 0]
    test_index_3 = 4
    assert not compare_and_swap(test_list_3, test_index_3)
    assert test_list_3 == [1, 3, 7, 6, 0], test_list_3

    test_list_4 = [1, 2, 3]
    test_index_4 = -1
    assert not compare_and_swap(test_list_4, test_index_4)
    assert test_list_4 == [1, 2, 3], test_list_4

    print("compare_and_swap tests passed")

def test_bubblesort_iterations():
    '''Tests if bubblesort algorithm by bubblesort function from bubblesort is being used correctly 
    to sort input lists.'''

    original_list = [2, 5, 0, 1, 2, 9]

    test_list_1 = original_list.copy()
    bubblesort(test_list_1, 1)
    assert test_list_1 == [2, 0, 1, 2, 5, 9], test_list_1

    test_list_2 = original_list.copy()
    bubblesort(test_list_2, 2)
    assert test_list_2 == [0, 1, 2, 2, 5, 9], test_list_2

    print("bubblesort iterations tests passed")

def test_bubblesort():
    '''Tests bubblesort function from bubble sort.'''

    test1 = []
    bubblesort(test1)
    assert test1 == [], test1

    test2 = [2, 4, 1, 7, 5]
    bubblesort(test2)
    assert test2 == [1, 2, 4, 5, 7], test2

    test3 = [3, 3, 3, 3]
    bubblesort(test3)
    assert test3 == [3, 3, 3, 3], test3

    test4 = [1, 2, 3, 4]
    bubblesort(test4)
    assert test4 == [1, 2, 3, 4], test4
    
    test5 = [6]
    bubblesort(test5)
    assert test5 == [6], test5
    
    print("bubblesort tests passed")

print()
test_compare_and_swap()
test_bubblesort_iterations()
test_bubblesort()
print()
