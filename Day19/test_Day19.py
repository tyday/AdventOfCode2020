import pytest
import Day19

def test_get_possibilities():
    rules = {0: '4 1 5', 1: '2 3 | 3 2', 2: '4 4 | 5 5', 3: '4 5 | 5 4', 4: 'a', 5: 'b', 6: '4 5'}
    assert Day19.get_possibilities(4, rules) == ['a']
    assert Day19.get_possibilities(6, rules) == ['ab']
    assert Day19.get_possibilities(2, rules) == ['aa','bb']
    assert Day19.get_possibilities(3, rules) == ['ab','ba']