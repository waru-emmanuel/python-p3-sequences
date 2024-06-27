#!/usr/bin/env python3

def print_fibonacci(length):
    '''function print_fibonacci()'''
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        fibonacci_sequence = [0, 1]
        for i in range(2, length):
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        print(fibonacci_sequence)
    









    
'''A Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. In mathematical terms, the Fibonacci series is defined by the recurrence relation:
F(n) = F(n-1) + F(n-2) for n > 1
where F(0) = 0 and F(1) = 1.

So, the Fibonacci series looks like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on. Each number in the sequence (after the first two) is the sum of the two preceding numbers.
'''