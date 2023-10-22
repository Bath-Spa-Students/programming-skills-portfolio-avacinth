# Exercise 6: Shrinking Guest List :ballot_box_with_check:

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

# Oh no, we can only invite two people because the new table cant make it on time.
print("Sorry, we can only invite two people to dinner.\n")

# Using pop() to remove guests from the list one at a time until only two names remain in the list.
while len(guests) > 2:
    name = guests.pop()
    print("Sorry, " + name + " there's no room at the table.")

# Telling people they're still invited.
for name in guests:
    print(name + ", you are still invited to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)