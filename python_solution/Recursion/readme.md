# Recurion

When we define some objects, we use some properties of these objects to define the objects. Actually, there are two principles for recursion.

1. Base cases which a terminating scenario that don't use the definition of itself.
2. Some rules to reduce all other case to base cases.

## In Computer science

We often use stacks of function to implement recursion. For example, to define [fibonacci sequence](!https://en.wikipedia.org/wiki/Fibonacci_number), we code wrtie code in python:

```python
def fib_num(n):
	if n== 0: return 0
	elif n == 1: return 1
	else: return fib_num(n-1) + fib_num(n-2)
```


 ** Divide and conquer** and **dynamic programming** are two programming tech using the idea of recursion.


