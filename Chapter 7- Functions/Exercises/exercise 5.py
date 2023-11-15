def describe_city (city, country = 'default country'):
    print (f"{city} is in {country}.")    #formatting

# Calling the function for three different cities
describe_city ('Amsterdam','Netherlands')
describe_city ('Paris', 'France')
describe_city ('New York')    #default country
