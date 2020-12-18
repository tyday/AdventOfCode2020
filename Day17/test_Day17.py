import pytest
import Day17

def test_parseInput():
    assert Day17.parseInput(
        '/home/pi/Programming/AdventOfCode/2020/Day17/test.txt'
        ) == {(1,0,0): {'status': True},
        (2,1,0): {'status': True},
        (0,2,0): {'status': True},
        (1,2,0): {'status': True},
        (2,2,0): {'status': True}
        }

def test_get_neighbors():
    assert len(Day17.get_neighbors((1,1,1))) == 26
    assert Day17.get_neighbors((0,0,0)) == [
        (-1, -1, -1), (-1, -1, 0), (-1, -1, 1), 
        (-1, 0, -1), (-1, 0, 0), (-1, 0, 1), 
        (-1, 1, -1), (-1, 1, 0), (-1, 1, 1), 
        (0, -1, -1), (0, -1, 0), (0, -1, 1), 
        (0, 0, -1), (0, 0, 1), 
        (0, 1, -1), (0, 1, 0), (0, 1, 1), 
        (1, -1, -1), (1, -1, 0), (1, -1, 1), 
        (1, 0, -1), (1, 0, 0), (1, 0, 1), 
        (1, 1, -1), (1, 1, 0), (1, 1, 1)]