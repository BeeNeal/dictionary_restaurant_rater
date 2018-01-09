import sys


def rate_restaurant(filename):
    """Restaurant rating lister."""

    # restaurant_roster = open(filename)
    restaurants = {}

    # for each line
    # right strip
    # split @ colon
    # put right into dictionary
    # index[0] will be key
    # index[1] will be value!

    with open(filename) as restaurant_roster:

        for line in restaurant_roster:
            establishment, rating = line.rstrip().split(":")

            restaurants[establishment] = rating

    for establishment, rating in sorted(restaurants.items()):
        print "{} is rated at {}.".format(establishment, rating)

    # restaurant_roster.close()

rate_restaurant(sys.argv[1])
