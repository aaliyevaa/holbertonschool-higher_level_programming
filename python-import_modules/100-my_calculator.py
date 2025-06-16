#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as c
    count = len(sys.argv)-1
    if count != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    operators = [ '+', '-', '*', '/']
    num1 = int(sys.argv[1])
    op = sys.argv[2]
    num2 = int(sys.argv[3])
    if op not in operators:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    if op == '+':
        print("{} {} {} = {}".format(num1, op, num2, c.add(num1, num2)))
    elif op == '-':
        print("{} {} {} = {}".format(num1, op, num2, c.sub(num1, num2)))
    elif op == '*':
        print("{} {} {} = {}".format(num1, op, num2, c.mul(num1, num2)))
    else:
        print("{} {} {} = {}".format(num1, op, num2, c.div(num1, num2)))
