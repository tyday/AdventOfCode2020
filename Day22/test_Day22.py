import pytest
import Day22

def test_get_data():
    assert Day22.get_data('/home/pi/Programming/AdventOfCode/2020/Day22/sample.txt') == [[9, 2, 6, 3, 1], [5, 8, 4, 7, 10]]

def test_play_game():
    decks = [[9, 2, 6, 3, 1], [5, 8, 4, 7, 10]]
    assert Day22.playGame(decks) == 306

def test_convert_deck_to_string():
    assert Day22.convert_decks_to_string([[9, 2, 6, 3, 1], [5, 8, 4, 7, 10]]) == 'p1 9 2 6 3 1p2 5 8 4 7 10'