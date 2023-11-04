pets = []

# Adding elements

pet = {
    'name': 'casper',
    'animal type': 'dog',
    'owner': 'kayla',
}
pets.append(pet)

pet = {
    'name': 'leo',
    'animal type': 'cat',
    'owner': 'liza',
}
pets.append(pet)

pet = {
    'name': 'lego',
    'animal type': 'rabbit',
    'owner': 'zuha',
}
pets.append(pet)

# For loop

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
