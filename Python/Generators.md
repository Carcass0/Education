A generator is a subclass of [[Iterators]].
A function that uses the yield keyword. 
Using next() returns the value at the next yield keyword, and pauses current execution.
If next() is run but no yields are left, raises StopIteration exception with the return value of the function appended.
Next runs the `__next__` [[Special attributes (Dunders)|magical method]].

Generator comprehensions are the same thing as list comprehensions but built with ().

Using yield from you can call generators inside a generator.

range() implementation with a generator function:
```python
def my_range(start, end):
	current = start
	while current < end:
		yield current
		current += 1

nums = my_range(1, 10)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
```
