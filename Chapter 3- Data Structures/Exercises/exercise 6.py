# Shrinking Guest List

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

# String variable
print("Sorry, we can only invite two people to dinner.\n")

# Removing guests
while len(guests) > 2:
    name = guests.pop()
    print("Sorry, " + name + " there's no room at the table.")

# Printing a message they are still invited
for name in guests:
    print(name + ", you are still invited to dinner.")

# Empty out the list
del(guests[0])
del(guests[0])

# Prove the list is empty
print(guests)
