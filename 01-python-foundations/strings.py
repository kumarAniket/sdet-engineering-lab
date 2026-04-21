my_string = "hello"

print("I'm going on a run")
print()
print('Hello\tWorld')
print(len("Hello I'm hungry"))
print()
print("----- Indexing & Slicing -----")
my_string = "Hello World"
# Indexing
print(my_string[0])
print(my_string[8])
print(my_string[-2])
# Slicing
print(my_string[2::1])
print(my_string[-3::- 1])
print(my_string[4:7])
print()

# Coding Excercise 3: String Indexing - Print letter 'r' from Hello World
print('Hello World'[-3])

# Coding Excercise 4: String Slicing - Grab 'ink' from tinker
print('tinker'[1:4])
print()
print("----- String Methods -----")
# String Methods

print("--- Concatenation ---")
my_string = "Pam"
new_string = "S" + my_string[1::1]
print(new_string)

print()
print("--- Split ---")
x="Hello World"
print(x.split())
print(x.split('o'))
print()
print("--- Print Formatting ---")
# Print-Formatting
print("Python {r}".format(r="rules!"))
name="Aniket"
print(f"Hello I'm {name}")