# Bit Manipulation
## Tricks

1. x & (x-1)
	
	Turn the rightest 1 in x binary form into 0.
	
2. x & (x+1)

	Turn the succession 1 from the rightest to the left into 0.
	
3. The properties of XOR

	* x ^ y = y ^ x
	* x ^ x = 0
	* x ^ 0 = x

## For Python

1. In leetcode, we get 32 bit integer numbers, while we return 62 bit integers in python code. It costs more attention for using bit manipulation in python.
	