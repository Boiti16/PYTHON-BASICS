#Strings
# A string is a sequence of characters enclosed in quotes, used to represent text.
# Strings can be defined using single quotes (' '), double quotes (" "), 
# or triple quotes (''' ''' or """ """).
# Strings are immutable, meaning they cannot be changed after creation.
# They can be concatenated using the + operator, repeated using the * operator,
# and sliced using indexing.


# Example of string creation and manipulation
my_string = "Hello, World!"
print(my_string)  # Output: Hello, World!


# String concatenation
another_string = " How are you?"
concatenated_string = my_string + another_string
print(concatenated_string)  # Output: Hello, World! How are you?


# String repetition
repeated_string = my_string * 2
print(repeated_string)  # Output: Hello, World!Hello, World!


# String slicing
sliced_string = my_string[0:5]  # Slicing from index 0 to 4
print(sliced_string)  # Output: Hello


# String length
string_length = len(my_string)
print(string_length)  # Output: 13


# String methods
# Strings have various built-in methods for manipulation.

uppercase_string = my_string.upper()  # Convert to uppercase
print(uppercase_string)  # Output: HELLO, WORLD!

lowercase_string = my_string.lower()  # Convert to lowercase
print(lowercase_string)  # Output: hello, world!

title_string = my_string.title()  # Convert to title case
print(title_string)  # Output: Hello, World!


# String replacement
replaced_string = my_string.replace("World", "Python")
print(replaced_string)  # Output: Hello, Python!


# String splitting
split_string = my_string.split(", ")  # Split by comma and space
print(split_string)  # Output: ['Hello', 'World!']


# String joining
joined_string = " ".join(split_string)  # Join with space
print(joined_string)  # Output: Hello World!


# String formatting
# Strings can be formatted using f-strings, format method, or % operator.

name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Alice and I am 30 years old.

formatted_string2 = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string2)  # Output: My name is Alice and I am 30 years old.

formatted_string3 = "My name is %s and I am %d years old." % (name, age)
print(formatted_string3)  # Output: My name is Alice and I am 30 years old.


# String indexing
# Strings can be indexed to access individual characters.

first_character = my_string[0]  # Accessing the first character
print(first_character)  # Output: H

last_character = my_string[-1]  # Accessing the last character
print(last_character)  # Output: !


# String escaping
# Special characters can be escaped using a backslash (\).

escaped_string = "He said, \"Hello!\""
print(escaped_string)  # Output: He said, "Hello!"


# Multiline strings

multiline_string = """This is a
multiline string.
It can span multiple lines."""
print(multiline_string) 

# Output: This is a
# multiline string.
# It can span multiple lines.
# String immutability
# Strings are immutable, meaning they cannot be changed after creation.
# Attempting to modify a string will result in an error.
