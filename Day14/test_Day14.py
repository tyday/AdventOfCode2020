import Day14
import pytest


def test_apply_mask_to_line_Part_two():
    mask, line = '000000000000000000000000000000X1001X', '42'
    assert Day14.apply_mask_to_line_Part_two(
        mask, line) == '000000000000000000000000000000X1101X'
    mask, line = '00000000000000000000000000000000X0XX', '26'
    assert Day14.apply_mask_to_line_Part_two(
        mask, line) == '00000000000000000000000000000001X0XX'


def test_get_address_permutations():
    assert Day14.get_address_permutations('000000111011') == ['000000111011']

    start = '000000000000000000000000000000X1101X'
    results = [
        '000000000000000000000000000000011010',  
        '000000000000000000000000000000011011',
        '000000000000000000000000000000111010',
        '000000000000000000000000000000111011'
    ]
    assert Day14.get_address_permutations(start).sort() == results.sort()

def test_partTwo():
    assert Day14.partTwo('/home/pi/Programming/AdventOfCode/2020/Day14/input_test_part_two.txt') == 208
