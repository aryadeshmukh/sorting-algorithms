from mergesort import merge
from mergesort import mergesort

def test_merge():
    '''Tests merge function from mergesort.'''

    test_1_1 = [1, 2, 5, 5, 6]
    test_1_2 = [3, 3, 4]
    assert (res1 := merge(test_1_1, test_1_2)) == [1, 2, 3, 3, 4, 5, 5, 6], res1

    test_2_1 = [1, 2, 3]
    test_2_2 = [4, 5, 6]
    assert (res2 := merge(test_2_1, test_2_2)) == [1, 2, 3, 4, 5, 6], res2

    test_3_1 = []
    test_3_2 = [1, 2]
    assert (res3 := merge(test_3_1, test_3_2)) == [1, 2], res3
    
    test_4_1 = [2, 2, 2, 2]
    test_4_2 = [1, 3]
    assert (res4 := merge(test_4_1, test_4_2)) == [1, 2, 2, 2, 2, 3], res4

    print("merge tests passed")

def test_mergesort():
    '''Tests the mergesort function from mergesort.'''

    test1 = []
    assert (res1 := mergesort(test1)) == [], res1

    test2 = [2, 4, 1, 7, 5]
    assert (res2 := mergesort(test2)) == [1, 2, 4, 5, 7], res2

    test3 = [3, 3, 3, 3]
    assert (res3 := mergesort(test3)) == test3, res3

    test4 = [1, 2, 3, 4]
    assert (res4 := mergesort(test4)) == test4, res4
    
    test5 = [6]
    assert (res5 := mergesort(test5)) == test5, res5
    
    print("mergesort tests passed")

print()
test_merge()
test_mergesort()
print()