from .mergesort import mergesort


def test_heapsort():
    assert mergesort([5, 3, 2, 1, 4]) == [1, 2, 3, 4, 5]


def test_heapsort_cmp():
    assert mergesort([5, 3, 2, 1, 4], lambda x, y: x > y) == [5, 4, 3, 2, 1]


def test_heapsort_custom_obj():
    assert mergesort(
        [{"id": 5}, {"id": 3}, {"id": 2}, {"id": 1}, {"id": 4}],
        lambda x, y: x["id"] <= y["id"],
    ) == [
        {"id": 1},
        {"id": 2},
        {"id": 3},
        {"id": 4},
        {"id": 5},
    ]
