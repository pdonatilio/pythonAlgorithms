# Fibonacci with Dynamic Programming and without recursive
# to feel the real difference
import time


def fibonacciWithoutDP(n):
    if n == 1 or n == 2:
        return 1
    return fibonacciWithoutDP(n - 1) + fibonacciWithoutDP(n - 2)


def fibonacciWithDP(n):
    if mem[n - 1] != -1:
        return mem[n - 1]
    mem[n - 1] = fibonacciWithDP(n - 1) + fibonacciWithDP(n - 2)
    return mem[n - 1]

#n = input('How the fibonacci number do you want to discover?')
n = 35

# to use with Dynamic Programming
# we create a mem list to keep the results finded
mem = [-1 for i in range(n)]
mem[0] = mem[1] = 1

print('Fibonacci with Dynamic Programming:', end='\t\t')
print(fibonacciWithDP(n), end=' - ')
print(str(time.clock()) + ' sec')

print('Fibonacci without Dynamic Programming:', end='\t')
print(fibonacciWithoutDP(n), end=' - ')
print(str(time.clock()) + ' sec')
