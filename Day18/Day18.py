from PartTwo.lexer import Lexer
from PartTwo.parser_ import Parser
from PartTwo.interpreter import Interpreter

def do_math(input1,input2,modifier):
    if modifier == '*':
        return int(input1) * int(input2)
    elif modifier == '+':
        return int(input1) + int(input2)
    else:
        raise Exception()

# def evaluate_maths(data=['1', '+', '2', '*', '3', '+', '4', '*', '5', '+', '6']):
def evaluate_maths(data='1 + 2 * 3 + 4 * 5 + 6'):
    modifier = '+'
    total = 0
    while len(data) > 0:
        input = data[0]
        data = data[1:]
        if input.isspace():
            pass
        elif input.isdigit():
            total = do_math(total,input,modifier)
        elif input == '*' or input == '+':
            modifier = input
        elif input == '(':
            side_total, data = evaluate_maths(data)
            total = do_math(side_total, total, modifier)
        elif input == ')':
            return total, data
        else:
            # Don't know what should go here
            raise Exception("Operation outside scope of evaluate_maths --", input)
    return total


def partOne():
    input = []
    with open('input.txt', 'r') as f:
        input = f.readlines()
    sum = 0
    for line in input:
        total = evaluate_maths(line)
        sum += total
    print(f"Total: {sum}")

def partTwo():
    input = ['1 + (2 * 3) + (4 * (5 + 6))']
    # with open('input.txt', 'r') as f:
    #     input = f.readlines()
    for line in input:
        lexer = Lexer(line)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        sum += value
    print(f"Total: {sum}")

partOne()