import sys


def rate_restaurant(filename):
    """Restaurant rating lister."""

    restaurant_roster = open(filename)
    restaurants = {}

    # for each line
    # right strip
    # split @ colon
    # put right into dictionary
    # index[0] will be key
    # index[1] will be value!

    for establishment in restaurant_roster:
        establishment = establishment.rstrip()
        establishment = establishment.split(":")

        restaurants[establishment[0]] = establishment[1]

    restaurants = restaurants.items()
    sorted_restaurants = sorted(restaurants)

    for establishment, rating in sorted_restaurants:
        print "{} is rated at {}.".format(establishment, rating)

print rate_restaurant(sys.argv[1])
