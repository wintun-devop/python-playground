""" print fuction """


hello_world="Hello world!"
print(hello_world)

# print for checking type
print(type(hello_world))

# Output: Hello World in printing multiple values
print("Hello", "World")  

# Custom separator
print("2025", "08", "17", sep="-")

# Custom end character
print("Loading", end="...")

#Print with str.join() for cleaner lists
items = ["apples", "bananas", "cherries"]
print(", ".join(items))  # Output: apples, bananas, cherries

#Print with formatting
name = "Win Tun"
age = 30
print(f"{name} is {age} years old.")  # Using f-string

# Print Unicode and emojis
print("Unicode test: \u2713")  # Output: Unicode test: ✓
print("Hello 🌏") 

def log_to_file()->str:
    with open("log.txt", "w") as f:
        print("Error occurred", file=f)

log_to_file()




