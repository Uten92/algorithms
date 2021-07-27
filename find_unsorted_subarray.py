import random


def find_unsorted_subarray(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            start_interval = i - 1
            break
    else:
        return [-1, -1]

    for i in range(start_interval + 1, len(array)):
        if array[i] >= array[start_interval]:
            end_interval = i - 1
            break
    else:
        end_interval = len(array) - 1

    return [start_interval, end_interval]


def test_find_unsorted_subarray_simple_case():
    array = [1, 4, 3, 2, 3, 4]
    result = find_unsorted_subarray(array)
    assert result == [1, 4]


def test_find_unsorted_subarray_in_sorted_array():
    array = sorted([random.randrange(100) for _ in range(random.randrange(100))])
    result = find_unsorted_subarray(array)
    assert result == [-1, -1]


def test_find_unsorted_subarray_in_empty_array():
    array = []
    result = find_unsorted_subarray(array)
    assert result == [-1, -1]


def test_find_unsorted_subarray_in_array_with_one_value():
    array = [random.randrange(100), ]
    result = find_unsorted_subarray(array)
    assert result == [-1, -1]


def test_find_unsorted_subarray_at_the_end_of_array():
    array = [1, 2, 5, 3]
    result = find_unsorted_subarray(array)
    assert result == [2, 3]
