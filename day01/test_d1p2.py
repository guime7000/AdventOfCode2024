from d1p2 import parse_locations_input, count_occurences, similarity_score


def test_build_locations_list():
    assert parse_locations_input('1234   6789') == (1234, 6789)


def test_count_occurences():
    left_loc = [1, 2, 3]
    right_loc = [1, 1, 2, 3, 3, 3]
    expected = {1: 2, 2: 1, 3: 3}
    assert count_occurences(left_loc, right_loc) == expected


def test_similarity_score():
    occurences = {1: 1, 2: 6, 4: 5}
    assert similarity_score(occurences) == 33
