# unittest framework:
create a class that inherits from unittest.TestCase and define methods for calling and asserting the target. To start the process: unittest.main()

## assertion methods:
.assertEqual(a, b)
.assertTrue(x)
.assertFalse(x)
.assertIs(a, b)
.assertIsNone(x)
.assertIn(a, b)
.assertIsInstance(a, b)
.assertRaises(err) - should be executed within a context manager

`.assertIs()`, `.assertIsNone()`, `.assertIn()`, and `.assertIsInstance()` all have opposite methods, named `.assertIsNot()`, and so forth.

## Fixtures:
#### Module-level fixtures
 Suppose you have a test module called `test_my_module.py`. In the `test_my_module.py`, the `setUpModule()` and `tearDownModule()` functions are the module-level fixtures.
- The `setUpModule()` function runs before all test methods in the test module.
- The `tearDownModule()` function runs after all methods in the test module.
#### Class-level fixtures
The `setUpClass()` and `tearDownClass()` are class-level fixtures:
- The `setUpClass()` runs before all test methods of a class
- The `tearDownClass()` runs after all test methods of a class.
#### Method-level fixtures
The `setUp()` and `tearDown()` are method-level fixtures:
- The `setUp()` runs before every test method in the test class.
- The `tearDown()` runs after every test method in the test class.

## unittest.mock
To mock objects, you use the `unittest.mock` module. The `unittest.mock` module provides the `Mock` class that allows you to mock other objects.

It also provides the `MagicMock` class that is a subclass of the `Mock` class. Besides the methods and properties of the `Mock` class, the `MagicMock` class has the implementations of all the dunder methods e.g., __str__ and __repr__.

example:
```python
from unittest.mock import Mock 
mock = Mock()
mock.api.return_value = { 'id': 1, 'message': 'hello' }
print(mock.api())
```

If you assign a property that doesn’t exist on the `Mock` object, Python will return a new mock object. Because of this dynamic, you can use the `Mock` class to mock any objects that you want.

# doctest module
1. Searches for text that looks like Python [interactive sessions](https://realpython.com/interacting-with-python/) in your documentation and docstrings
2. Parses those pieces of text to distinguish between executable code and expected results
3. Runs the executable code like regular Python code
4. Compares the execution result with the expected result


- Tests start after the **`>>>` prompt** and continue with the **`...` prompt**, just like in a Python interactive session.
- **Expected outputs** must occupy the line or lines immediately after the test.
- Outputs sent to the **standard output stream** are captured.
- Outputs sent to the **standard error stream** aren’t captured.
- The **column** at which a test starts doesn’t matter as long as the expected output is at the same level of indentation.

Can run programmatically by using testfile or testmod, or from console by using python  -m doctest (-v) name.format (py, md, txt)