### Frequently Used Built-in Functions
- print()                   Output text to console                  print("Hello, Win!")
- len()                     Get length of iterable                  len([1, 2, 3])
- type()                    Check data type                         type("hello")
- range()                   Generate sequence of numbers            for i in range(5):
- int(),float(),str()       Type conversion                         int("42"), str(3.14)
- input()                   Get user input                          name = input("Your name: ")
- sum()                     Add elements of iterable                sum([1, 2, 3])
- max(),min()               Find largest/smallest value             max([4, 7, 2])
- sorted()                  Return sorted list                      sorted([3, 1, 2])
- enumerate()               Index + value in loop                   for i, val in enumerate(lst)
- zip()                     Combine iterables                       zip(list1, list2)
- map()                     Apply function to iterable              map(str.upper, names)
- filter()                  Filter iterable with condition          filter(is_even, nums)
- any(), all()              Logical checks on iterables             any([True, False])
- isinstance()              Type checking                           isinstance(x, int)              

### Utility & Debugging Functions

- id() – Get memory address of object
- dir() – List attributes of object
- help() – Access documentation
- eval() – Evaluate string as Python expression
- exec() – Execute dynamic Python code


### print function basic syntax
```
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```
- Parameters
    - *objects: One or more values to print. Can be strings, numbers, lists, etc.
    - sep: Separator between objects (default is a space ' ').
    - end: What to print at the end (default is newline '\n').
    - file: Where to send the output (default is sys.stdout, but can be a file).
    - flush: Whether to forcibly flush the output buffer (default is False).