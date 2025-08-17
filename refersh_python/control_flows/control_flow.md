### Main Types of Control Flow in Python
- Conditional Statements (if, elif, else)
- Loops (for, while)
- Control Statements Inside Loops
   - break  	    Exit the loop early	if x == 5: break
   - continue   	Skip current iteration	if x % 2 == 0: continue
   - pass	        Placeholder for future code	if x < 0: pass
- Function-Based Control Flow
```
def check_even(x):
    if x % 2 == 0:
        return True
    return False
```
- Exception Handling (try, except, finally)
```
try:
    risky_operation()
except ValueError:
    handle_error()
finally:
    cleanup()
```
- Advanced Control Flow Tools
    - match / case (Python 3.10+)
    ```
    match command:
        case "start":
            print("Starting")
        case "stop":
            print("Stopping")

    ```

### Summary for Control Flow

- Conditional	            if, elif, else	                Decision-making
- Looping	                for, while	                    Repetition
- Loop Control	            break, continue, pass	        Modify loop behavior
- Function Control	        def, return	                    Encapsulate logic
- Pattern Matching	        match, case	                    Structured decisions
- Exception Handling	    try, except, finally,           raise	Error management