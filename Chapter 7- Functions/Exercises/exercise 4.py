def make_shirt (size = 'large', message = 'I Love Python!'):
    print(f"Creating a {size} shirt with the message: {message}")

# default message
make_shirt()

# medium shirt with the default message
make_shirt(size = 'medium')

# shirt of any size with a different message
make_shirt(size = 'small', message = 'Its me, hi.')
