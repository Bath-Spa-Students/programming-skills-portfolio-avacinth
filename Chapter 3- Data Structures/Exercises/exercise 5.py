# Exercise 5: Change Guest List :ballot_box_with_check:

# Inviting people to dinner.
guests = ['Sofia Borcelo', 'Shaima Francisco', 'Myen Naguit', 'RJ Tobias', 'Erich Lubis']

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

# Myen can't make it! Let's invite Yumi instead.
del(guests[1])
guests.insert(1, 'Yumi Molina')

# Changing the guest list.
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