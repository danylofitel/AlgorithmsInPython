__author__ = 'Danylo'


# http://www.geeksforgeeks.org/find-all-possible-outcomes-of-a-given-expression/
# Find all possible outcomes of a given expression
# Given an arithmetic expression, find all possible outcomes of this expression.
# Different outcomes are evaluated by putting brackets at different places.
# We may assume that the numbers are single digit numbers in given expression.


def eval_expr(operand1, op, operand2):
    if op == '+':
        return operand1 + operand2
    elif op == '-':
        return operand1 - operand2
    elif op == '*':
        return operand1 * operand2
    elif op == '/':
        return operand1 / operand2
    elif op == '**':
        return operand1 ** operand2
    return None


def all_outcomes(expr, left, right):
    # If there is only one character, it must
    # be a digit (or operand), return it.

    if left == right:
        return [expr[left]]

    # If there are only three elements, middle
    # one must be operator and corner ones must be operand
    if left + 2 == right:
        return [eval_expr(expr[left], expr[left + 1], expr[right])]

    res = []
    # every i refers to an operator
    for i in range(left + 1, right + 1, 2):
        # l refers to all the possible values
        # in the left of operator 'expr[i]'
        l = all_outcomes(expr, left, i - 1)

        # r refers to all the possible values
        # in the right of operator 'expr[i]'
        r = all_outcomes(expr, i + 1, right)

        # Take above evaluated all possible
        # values in left side of 'i'
        for s1 in range(0, len(l)):
            # Take above evaluated all possible
            # values in right side of 'i'
            for s2 in range(0, len(r)):
                # Calculate value for every pair
                # and add the value to result.
                val = eval_expr(l[s1], expr[i], r[s2])
                res.append(val)

    return res

expressions = [
    [1, '+', 3, '*', 2],
    [1, '*', 2, '+', 3, '*', 4],
    [1.0, '-', 2.0, '+', 3.0, '*', 4.0, '/', 5.0, '**', 6.0]
]

for expr in expressions:
    print all_outcomes(expr, 0, len(expr) - 1)
