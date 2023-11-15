# Create a list

sandwich_orders = ["pastrami", "chicken", "egg", "ham", "cheese", "prawn", "meatball", "tuna"]

finished_sandwiches = []

print ("The Deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove ('pastrami')

print ()
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made you your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title() + " is done")
