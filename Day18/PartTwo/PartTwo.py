from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

def partTwo():
    input = ['1 + (2 * 3) + (4 * (5 + 6))']
    with open('/home/pi/Programming/AdventOfCode/2020/Day18/input.txt', 'r') as f:
        input = f.readlines()
    sum = 0.0
    for line in input:
        lexer = Lexer(line)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        sum += value.value
    print(f"Total: {sum}")

partTwo()