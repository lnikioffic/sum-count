from main import sum_count


def test_empty_array():
    assert sum_count([]) == (0, 0)

def test_no_even_positives():
    assert sum_count([1, 3, 5, -2, -4]) == (0, 0)

def test_all_even_positives():
    assert sum_count([2, 4, 6, 8]) == (4, 20)

def test_mixed_array():
    assert sum_count([1, 2, 3, 4, 5, 6, -2, -4, 8, 10]) == (5, 30)
