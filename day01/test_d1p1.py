from d1p1 import parse_locations_input, compute_distance


def test_build_locations_list():
    assert parse_locations_input('1234   6789') == (1234, 6789)


def test_compute_distance():
    assert compute_distance([1, 3], [2, 6]) == [1, 3]
