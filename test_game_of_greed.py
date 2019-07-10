from game_of_greed import


# test_zilch - non scoring roll should return 0

def test_zilch():
    expected = 0
    actual = round_score(0)
    assert expected == actual

# test_ones - rolls with various number of 1s should return correct score

def test_ones():
    expected = 100
    
# test_twos - rolls with various number of 2s should return correct score

def test_two():
    expected = 2
    actual = (2)
    assert expected == actual

# test_threes - rolls with various number of 3s should return correct score

# test_fours - rolls with various number of 4s should return correct score

# test_fives - rolls with various number of 5s should return correct score

# test_sixes - rolls with various number of 6s should return correct score

# test_straight - 1,2,3,4,5,6 should return correct score

# test_three_pairs - 3 pairs should return correct score

# test_leftover_ones - 1s not used in set of 3 (or greater) should return correct score

# test_leftover_fives - 5s not used in set of 3 (or greater) should return correct score

# test_two_trios = 2 sets of 3 should return correct score

# test_roll -doing a roll with x number of dice should return sequence of x length random integers between 1 and 6 inclusive
