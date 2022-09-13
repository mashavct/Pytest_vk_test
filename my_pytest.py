import pytest


#Тест проверяет функцию sum, суммирующие числа в списке
pytest.mark.parametrize(('test_list', 'test_sum'), [([1], 1), ([1,-1], 0), ([3,2], 5),([1, None], None)])
def test_list_sum_int_negative_case(test_list, test_sum):
    try:
        assert sum(test_list) == test_sum
    except TypeError:
        pass

#Тест проверяет функцию len, считающую длину списка
@pytest.mark.parametrize(('test_list', 'test_size'), [([1], 1), ([1,-1], 2), ([3,2,4], 3),([], 0)])
def test_list_size(test_list, test_size):
    assert len(test_list) == test_size


#Тест проверяет функцию sorted, сортирующую список
@pytest.mark.parametrize(('sraeted_list', 'sorted_list'), [([1], [1]), ([2,1], [1,2]), ([-1,-2], [-2,-1])])
def test_list_sort(sraeted_list, sorted_list):
    assert sorted(sraeted_list) == sorted_list

#Тест проверяет функцию sum, суммирующие числа в множестве
@pytest.mark.parametrize(('test_set', 'test_sum'), [(set([1]), 1), (set([1,-1]), 0), (set([3,2]), 5),(set([1, None]), None)])
def test_set_sum_int_negative_case(test_set, test_sum):
    try:
        assert sum(test_set) == test_sum
    except TypeError:
        pass

#Тест проверяет функцию len, считающую длину множества
@pytest.mark.parametrize(('test_set', 'test_size'), [(set([1]), 1), (set([1,-1]), 2), (set([3,2,3]), 2),(set([]), 0)])
def test_set_size(test_set, test_size):
    assert len(test_set) == test_size

#Тест проверяет конструктор множества на предмет того, что в множество действительно попадают элементы исходного списка
@pytest.mark.parametrize(('test_set', 'contained_element'), [(set([1]), 1), (set([-1,-2]), -2), (set([3,2,3]), 3)])    
def test_set_contains(test_set, contained_element):
    assert contained_element in test_set
