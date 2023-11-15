# Create a list

sandwich_orders = ["chicken", "egg", "ham", "cheese", "prawn", "meatball", "tuna"]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made you your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title() + " is done")
