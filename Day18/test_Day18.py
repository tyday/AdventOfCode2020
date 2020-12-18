import pytest
import Day18

def test_evaluate_maths():
    assert Day18.evaluate_maths('2 * 3 + (4 * 5)') == 26
    assert Day18.evaluate_maths('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437
    assert Day18.evaluate_maths('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240
    assert Day18.evaluate_maths('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632
