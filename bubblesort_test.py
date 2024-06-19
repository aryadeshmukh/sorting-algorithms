import pytest
from typing import List
from bubblesort import bubblesort
from bubblesort import _bubblesort
from bubblesort import compare_and_swap

class TestBubblesort:
    @pytest.fixture
    def dummy_list(self) -> List[int]:
        return [1, 2, 3]

    def test_compare_and_swap_execute_swap(self) -> None:
        '''Tests compare_and_swap when specified values are in incorrect order.'''
        test_list = [1, 5, 4, 6]
        test_index = 1
        assert compare_and_swap(test_list, test_index)
        assert test_list == [1, 4, 5, 6], test_list
    
    def test_compare_and_swap_no_swap(self, dummy_list) -> None:
        '''Tests compare_and_swap when specified values are in correct order.'''
        test_index = 0
        assert not compare_and_swap(dummy_list, test_index)
        assert dummy_list == [1, 2, 3], dummy_list
    
    def test_compare_and_swap_index_out_or_range(self) -> None:
        '''Tests compare_and_swap when index is out or range.'''
        test_list = [1, 3, 7, 6, 0]
        test_index = 4
        assert not compare_and_swap(test_list, test_index)
        assert test_list == [1, 3, 7, 6, 0], test_list
    
    def test_compare_and_swap_negative_index(self, dummy_list: List[int]) -> None:
        '''Tests compare_and_swap when index is negative.'''
        test_index = -1
        assert not compare_and_swap(dummy_list, test_index)
        assert dummy_list == [1, 2, 3], dummy_list
    
    @pytest.fixture(scope="class")
    def iterations_list(self) -> List[int]:
        return [2, 5, 0, 1, 2, 9]
    
    def test_bubblesort_one_iteration(self, iterations_list: List[int]) -> None:
        '''Tests first iteration of bubblesort.'''
        _bubblesort(iterations_list, 1)
        assert iterations_list == [2, 0, 1, 2, 5, 9], iterations_list
    
    def test_bubblesort_next_iteration(self, iterations_list: List[int]) -> None:
        '''Tests next iterations of bubblesort on result from test_bubblesort_one_iteration.'''
        _bubblesort(iterations_list, 1)
        assert iterations_list == [0, 1, 2, 2, 5, 9], iterations_list
    
    def test_sort_empty_list(self) -> None:
        '''Tests bubblesort on empty list.'''
        test = []
        bubblesort(test)
        assert test == [], test
    
    @pytest.mark.parametrize("test_input, expected", [
        ([2, 4, 1, 7, 5], [1, 2, 4, 5, 7]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([4, 0, -2, 13, 9], [-2, 0, 4, 9, 13])])
    def test_sort_basic_lists(self, test_input: List[int], expected: List[int]) -> None:
        '''Tests bubblesort on basic lists.'''
        bubblesort(test_input)
        assert test_input == expected, test_input

    def test_sort_repeating_list(self) -> None:
        '''Tests bubblesort on list containing only one unique element.'''
        test = [3, 3, 3, 3]
        bubblesort(test)
        assert test == [3, 3, 3, 3], test
    
    def test_already_sorted_list(self) -> None:
        '''Tests bubblesort on already sorted list.'''
        test = [1, 2, 3, 4]
        bubblesort(test)
        assert test == [1, 2, 3, 4], test

    def test_length_one_list(self) -> None:
        '''Tests bubblesort on a list with only one element.'''
        test = [6]
        bubblesort(test)
        assert test == [6], test