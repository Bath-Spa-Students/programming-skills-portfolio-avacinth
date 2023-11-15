# Change Guest List

# List inviting people to dinner
guests = ['Sofia Borcelo', 'Shaima Francisco', 'Myen Naguit', 'RJ Tobias', 'Erich Lubis']

# List index + message
name = guests[0]
print(name + ", I would like to invite you to dinner.")

name = guests[1]
print(name + ", I would like to invite you to dinner.")

name = guests[2]
print(name + ", I would like to invite you to dinner.")

name = guests[3]
print(name + ", I would like to invite you to dinner.")

name = guests[4]
print(name + ", I would like to invite you to dinner.")

name = guests[1]
print("\nSorry, " + name + " can't make it to dinner.")

# Changing the guest list
del(guests[1])
guests.insert(1, 'Yumi Molina')

# Updated invites
name = guests[0]
print("\n" + name + ", I would like to invite you to dinner.")

name = guests[1]
print(name + ", I would like to invite you to dinner.")

name = guests[2]
print(name + ", I would like to invite you to dinner.")

name = guests[3]
print(name + ", I would like to invite you to dinner.")

name = guests[4]
print(name + ", I would like to invite you to dinner.")
