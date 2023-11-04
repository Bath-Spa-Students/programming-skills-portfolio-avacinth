# Dictionaries

rivers = {
    'nile': 'egypt',
    'danube': 'germany',
    'amazon': 'brazil',
    'rhine': 'france',
    'mekong': 'myanmar',
    }

# For loop

for river, country in rivers.items():
    print("\nThe " + river.title() + " flows through " + country.title() + ".")

print("\nThe following are rivers included in the data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following are countries included in the data set:")
for country in rivers.values():
    print("- " + country.title())
