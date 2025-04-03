import sqlite3

# Connect to database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Define easy-level questions
easy_questions = [
    ("easy", "I/O Operations", "What function is used to display text on the screen in Python?", "print()", "display()", "echo()", "show()", "A", "The print() function is used to display output."),
    ("easy", "Variables", "How do you store a number in a variable?", "number = 5", "num(5)", "store 5", "set number = 5", "A", "In Python, variables are assigned using '=' like 'number = 5'."),
    ("easy", "Built-in Functions", "What does the len() function do?", "Returns the length of a string or list", "Counts numbers", "Measures time", "None of the above", "A", "The len() function returns the number of elements in a list or the length of a string."),
    ("easy", "Functions", "Which keyword is used to create a function?", "def", "function", "create", "define", "A", "In Python, functions are defined using the 'def' keyword."),
    ("easy", "Strings", "What will print(3 * 'Hello') output?", "'HelloHelloHello'", "'Hello3'", "'Hello*3'", "Error", "A", "The * operator repeats the string 3 times."),
    ("easy", "Syntax", "How do you write a comment in Python?", "# This is a comment", "// This is a comment", "/* This is a comment */", "<!-- Comment -->", "A", "Python uses '#' for single-line comments."),
    ("easy", "Input/Output", "What type of data does input() give you?", "String", "Integer", "Float", "Boolean", "A", "The input() function always returns a string."),
    ("easy", "Error Handling", "What happens if you divide by zero in Python?", "Error", "Returns 0", "Returns Infinity", "Ignores the operation", "A", "Python raises a ZeroDivisionError when dividing by zero."),
    ("easy", "Data Types", "How do you check what type of data a variable holds?", "type()", "typeof()", "checktype()", "varType()", "A", "The type() function returns the data type of a variable."),
    ("easy", "Loops", "What does range(5) produce?", "0, 1, 2, 3, 4", "1, 2, 3, 4, 5", "0, 1, 2, 3, 4, 5", "None of the above", "A", "The range(5) function generates numbers from 0 to 4."),
    ("easy", "Strings", "What will print('5' + '3') display?", "'53'", "'8'", "'5 3'", "Error", "A", "Strings concatenate when using '+', so '5' + '3' results in '53'."),
    ("easy", "Lists", "How do you get the last item of a list in Python?", "list[-1]", "list[0]", "list[last]", "list.end()", "A", "Using list[-1] accesses the last item in a list."),
    ("easy", "Loops", "What is a for loop used for?", "Repeating actions", "Defining functions", "Creating lists", "Handling errors", "A", "A for loop iterates over elements in a sequence."),
    ("easy", "File I/O", "How do you open a file to read its content?", "open(filename, 'r')", "open(filename, 'w')", "open(filename, 'a')", "open(filename)", "A", "Using 'r' opens a file for reading."),
    ("easy", "Type Conversion", "How do you change the string '10' into a number?", "int('10')", "string(10)", "toInt('10')", "convert('10')", "A", "int('10') converts the string '10' to an integer."),
    ("easy", "Lists", "What does the append() function do to a list?", "Adds an element to the end", "Removes an element", "Sorts the list", "Clears the list", "A", "The append() method adds an item to the end of a list."),
    ("easy", "Operators", "What is the difference between = and ==?", "= assigns a value, == compares", "= compares, == assigns a value", "Both are the same", "Neither are valid", "A", "= assigns a value, while == checks equality."),
    ("easy", "Lists", "How do you check if a word is in a list?", "'word' in list", "'word'.contains(list)", "list.has('word')", "find('word', list)", "A", "The 'in' keyword checks for membership in a list."),
    ("easy", "Operators", "What will print(5 / 2) output?", "2.5", "2", "3", "Error", "A", "Python performs true division by default, returning 2.5.")
]


# Define medium-level questions
medium_questions = [
    ("medium", "Data Cleaning", "What does strip() do to a string?", "Removes whitespace from both ends", "Converts to uppercase", "Splits string into a list", "Removes all vowels", "A", "strip() removes leading and trailing whitespace."),
    ("medium", "Dictionaries", "How do you create a dictionary?", "{'key': 'value'}", "[key, value]", "dict(key, value)", "('key', 'value')", "A", "A dictionary is created using curly brackets `{}` with key-value pairs."),
    ("medium", "Lists", "What is the difference between pop() and remove() in a list?", "pop() removes by index, remove() by value", "Both do the same thing", "pop() deletes all elements", "remove() can only delete the first element", "A", "pop() removes an item at a specific index, while remove() deletes by value."),
    ("medium", "Dictionaries", "How do you loop through a dictionary’s keys and values?", "for k, v in dict.items()", "for k, v in dict.iter()", "for dict.loop()", "for each in dict", "A", "The `items()` method allows iterating over key-value pairs."),
    ("medium", "Sets", "What does set() do?", "Creates a unique collection of elements", "Sorts a list", "Merges dictionaries", "Creates a new variable", "A", "`set()` creates a collection of unique, unordered elements."),
    ("medium", "Lists", "How can you reverse a list in Python?", "list[::-1]", "list.reverse()", "Both A and B", "list.flip()", "C", "Both slicing (`[::-1]`) and `.reverse()` can reverse a list."),
    ("medium", "Loops", "What does enumerate() help with in loops?", "Provides an index with values", "Sorts the list", "Removes duplicates", "Finds prime numbers", "A", "enumerate() generates an index along with items in a loop."),
    ("medium", "Error Handling", "How do you handle errors in Python?", "Using try-except", "Using if-else", "Using a loop", "You cannot handle errors", "A", "try-except blocks handle errors gracefully."),
    ("medium", "Dictionaries", "How do you combine two lists into a dictionary?", "Using zip()", "Using dict(list1, list2)", "Using merge()", "Using extend()", "A", "zip() pairs elements from two lists into key-value pairs."),
    ("medium", "Strings", "What does join() do in strings?", "Combines a list into a string", "Splits a string", "Removes spaces", "Reverses a string", "A", "join() merges list elements into a single string."),
    ("medium", "Copying Objects", "What is the difference between copy() and deepcopy()?", "deepcopy() copies nested objects", "copy() copies nested objects", "They are the same", "copy() removes duplicates", "A", "deepcopy() creates a separate copy of nested structures."),
    ("medium", "Lists", "How do you combine two lists so that each pair of items matches up?", "Using zip()", "Using join()", "Using map()", "Using combine()", "A", "zip() matches elements from two lists."),
    ("medium", "Functions", "How do you create a quick function using lambda?", "lambda x: x * 2", "quick_func(x) = x * 2", "def lambda x: x * 2", "lambda(x) = x * 2", "A", "Lambda functions are anonymous functions."),
    ("medium", "Comprehensions", "What will [x for x in range(5) if x % 2 == 0] produce?", "[0, 2, 4]", "[1, 3, 5]", "[0, 1, 2, 3, 4]", "[2, 4]", "A", "This list comprehension filters even numbers."),
    ("medium", "Lists", "How do you remove duplicate values from a list?", "Using set()", "Using list.remove()", "Using unique()", "Using filter()", "A", "Converting a list to a set removes duplicates."),
    ("medium", "Functions", "What do *args and **kwargs do in a function?", "Allow variable arguments", "Create new functions", "Force keyword arguments", "Are used for recursion", "A", "`*args` accepts variable positional arguments, `**kwargs` allows keyword arguments."),
    ("medium", "Data Types", "What is the difference between mutable and immutable?", "Mutable can change, immutable cannot", "Both can be changed", "Immutable means no indexing", "Mutable means read-only", "A", "Mutable objects (lists) can be modified, immutable ones (tuples) cannot."),
    ("medium", "Data Types", "What is the difference between a list and a tuple?", "Lists are mutable, tuples are immutable", "Tuples are faster", "Lists store strings, tuples store numbers", "Lists are smaller than tuples", "A", "Lists allow changes, tuples do not."),
    ("medium", "Lists", "What is the difference between .extend() and .append() in lists?", "extend() adds multiple items, append() adds one", "append() removes items", "extend() deletes the last item", "append() sorts the list", "A", "extend() adds multiple elements, append() adds one."),
    ("medium", "OOP", "How do you create your own type of object using class?", "Using class MyClass:", "Using create MyClass()", "Using new MyClass", "Using def class MyClass:", "A", "Classes are defined using `class MyClass:`."),
]

# Define hard-level questions
hard_questions = [
    ("hard", "I/O Operations", "What is the difference between copying a list and making a deep copy?", "deepcopy() copies nested objects", "copy() copies deeply", "copy() removes duplicates", "Both are the same", "A", "deepcopy() copies all nested objects, while copy() is shallow."),
    ("hard", "OOP", "What is __init__ used for in a class?", "Initializes an object", "Deletes an object", "Imports a module", "Creates a function", "A", "__init__ is a constructor method that initializes an object when created."),
    ("hard", "Generators", "What is a Python generator, and why is it useful?", "A function that yields values lazily", "A function that returns a list", "A function that runs in the background", "A function that prints values", "A", "Generators produce values lazily using `yield`, improving performance."),
    ("hard", "Generators", "What does yield do in a function?", "Pauses execution and saves state", "Ends the function", "Returns multiple values at once", "Creates a list", "A", "`yield` pauses function execution and resumes when called."),
    ("hard", "Recursion", "How do you prevent a function from running forever in recursion?", "Use a base case", "Use a loop", "Call return at the end", "Recursion stops automatically", "A", "A base case prevents infinite recursion."),
    ("hard", "Caching", "What is caching, and how can it help your code run faster?", "Stores frequently used data", "Deletes unused data", "Replaces variables", "Slows down execution", "A", "Caching stores frequently used data to avoid redundant calculations."),
    ("hard", "OOP", "What does the @staticmethod decorator do?", "Defines a method that doesn’t use self", "Defines a private method", "Makes a method return an integer", "Creates a new object", "A", "The @staticmethod decorator defines a function inside a class that doesn't access instance attributes."),
    ("hard", "Memory Management", "How does Python clean up variables it no longer needs?", "Garbage collection", "Deletes them manually", "Replaces them with new data", "Moves them to disk", "A", "Python’s garbage collector automatically removes unused variables."),
    ("hard", "Metaclasses", "What is a metaclass in Python?", "A class that defines class behavior", "A template for objects", "A function that runs in the background", "A subclass of all classes", "A", "Metaclasses control how classes are created and behave."),
    ("hard", "Concurrency", "How does Python handle multiple things running at once (multithreading)?", "Threading module", "Parallel execution by default", "Multiple CPUs for each thread", "It doesn’t support multithreading", "A", "Python uses the threading module but has limitations due to the GIL."),
    ("hard", "Concurrency", "What is the Global Interpreter Lock (GIL), and why does it matter?", "It limits Python threads to one execution at a time", "It makes Python run faster", "It locks variables from being changed", "It runs code in the background", "A", "The GIL allows only one thread to execute at a time in CPython."),
    ("hard", "Serialization", "How do you save and load data using serialization?", "Using pickle", "Using zip()", "Using import", "Using serialize()", "A", "The pickle module allows saving and loading objects in Python."),
    ("hard", "Operators", "What is the difference between is and ==?", "is checks identity, == checks value", "They are the same", "is checks value, == checks memory", "Both are for comparisons", "A", "`is` checks if two variables reference the same object, `==` checks if values are equal."),
    ("hard", "OOP", "How do you make an object that can be looped over?", "Implement __iter__", "Use a list", "Define __call__", "Use a while loop", "A", "Implementing `__iter__` and `__next__` allows an object to be iterable."),
    ("hard", "OOP", "What is method overriding, and why is it useful?", "Redefining a method in a subclass", "Creating a new method", "Changing a function’s return type", "Using two methods at once", "A", "Method overriding allows a subclass to change the behavior of a parent method."),
    ("hard", "Caching", "What is functools.lru_cache, and how does it help?", "Caches function results", "Runs code faster", "Deletes unused variables", "Replaces a function", "A", "functools.lru_cache caches function results to improve performance."),
    ("hard", "Context Managers", "What is a context manager, and how does it help manage files?", "Handles resource allocation with `with`", "Manages global variables", "Creates new files automatically", "Speeds up execution", "A", "Context managers use `with` to ensure proper file handling."),
    ("hard", "Modules", "How do you avoid errors when two files import each other?", "Use import inside functions", "Remove all imports", "Use a while loop", "Use import as", "A", "Placing imports inside functions prevents circular dependencies."),
    ("hard", "Data Classes", "What are dataclasses, and why are they useful?", "A way to define structured data", "A way to format data as JSON", "A method to store database entries", "A replacement for lists", "A", "Dataclasses provide an easy way to create structured data objects.")
]

# Insert questions into the database
cursor.executemany("""
    INSERT INTO quiz_questions (category, topic, question, option_a, option_b, option_c, option_d, correct_answer, explanation)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", easy_questions)

cursor.executemany("""
    INSERT INTO quiz_questions (category, topic, question, option_a, option_b, option_c, option_d, correct_answer, explanation)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", medium_questions)

cursor.executemany("""
    INSERT INTO quiz_questions (category, topic, question, option_a, option_b, option_c, option_d, correct_answer, explanation)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", hard_questions)

# Commit and close connection
conn.commit()
conn.close()

print("Easy, Medium, and Hard questions inserted successfully with topics!")


