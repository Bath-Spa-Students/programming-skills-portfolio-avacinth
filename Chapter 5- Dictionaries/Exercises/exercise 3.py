# Dictionaries

glossary = {
    'String': 'A data type that presents a sequence of characters in quotes.',
    'Integer': 'used to represent whole numbers, both positive and negative.',
    'Float': 'Used to represent numbers with decimal points.',
    'Boolean': 'Can have one of two values: True or False.',
    'List': 'Stores a collection of items in an ordered sequence.',
    'Loop': 'Allows a set of instructions to be repeated.',
    'Variable': 'Where data can be stored and retrieved.',
    'Function': 'A reusable block of code.',
    'Dictionary': 'Stores a collection of key-value pairs.',
    'Key': 'First item in a key-value pair in a dictionary.',
    }

# For loop

for word, definition in glossary.items():
    print("\n" + word + ": " + definition)
