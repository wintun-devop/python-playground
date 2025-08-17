### Looping Processes
### Loop Constructs: The actual syntax and structure used to define loops (for, while, etc.)
- for               Definite iteration           Iterates over a known sequence (like a list, range, or generator).
- while             Indefinite iteration         Continues as long as a condition remains true.
- do-while          Post-condition loop          Executes at least once before checking the condition (not native in Python).


-  Python doesn’t have a built-in do-while, but you can simulate it like this:
```
while True:
    # do something
    if not condition:
        break
```


