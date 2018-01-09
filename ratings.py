import sys
import random


def read_restaurant(restaurants):
    """Restaurant rating lister."""

    # restaurant_roster = open(filename)


    # for each line
    # right strip
    # split @ colon
    # put right into dictionary
    # index[0] will be key
    # index[1] will be value!

    for establishment, rating in sorted(restaurants.items()):
        print "{} is rated at {}.".format(establishment, rating)


def add_restaurant(restaurants):
    new_restaurant = raw_input("Is there a restaurant we're missing? \n"
    "Add it for Ratings Points! \n"
    "Restaurant name: ")

    while True:
        new_restaurant_rating = raw_input("Your rating: ")

        if 0 < int(new_restaurant_rating) < 6:
            restaurants[new_restaurant] = new_restaurant_rating
            break
        else:
            print "Please enter a number rating between 1 and 5"

    return restaurants

    # restaurant_roster.close()

def edit_rating_rand(restaurants):
    """Allow user to edit rating of random restaurant in restaurants{}"""

    random_restaurant = random.choice(restaurants.keys())
    print random_restaurant
    while True:
        user_rating = raw_input("What should the rating be for {}?".format(random_restaurant))

        if 0 < int(user_rating) < 6:
            restaurants[random_restaurant] = user_rating
            print "Rating updated!"
            break
        else:
            print "Please enter a number rating between 1 and 5"

    return restaurants

def edit_rating(restaurants):
    """Allow user to select a restaurant and edit its rating"""

    chosen_restaurant = raw_input("Please select a restaurant rating to update!")

    undercase_restaurants = [k.lower() for k in restaurants]

    while True:
# FIXME - need to check using .get() whether key exists to update
        if chosen_restaurant.lower() in undercase_restaurants:
            new_rating = raw_input("New rating: ")
            if 0 < int(new_rating) < 6:
                restaurants[chosen_restaurant] = new_rating
                break
            else:
                print "That's not in our system. Would you like to add it?"
                user_choice = raw_input("Yes or no: ")
                if user_choice.lower() == 'yes':
                    add_restaurant(restaurants)
                else:
                    break
    return restaurants

def start_restaurant_rater():

    filename = sys.argv[1]

    restaurants = {}

    with open(filename) as restaurant_roster:

        for line in restaurant_roster:
            establishment, rating = line.rstrip().split(":")

            restaurants[establishment] = rating

    print ("Hello! Welcome to the Restaurant Rater. Type 'a' to see all ratings. \n"
    "Type 'b' to add a new restaurant and rate it. \n"
    "Type 'c' to edit a random restaurant's rating. \n"
    "Type 'd' to edit a selected restaurant's rating \n"
    "Type 'q' to quit. \n")

    while True:
        user_choice = raw_input("type 'a', 'b', c, or 'q': ")

        if user_choice.lower() == 'q':
            break

        elif user_choice.lower() == 'a':
            read_restaurant(restaurants)

        elif user_choice.lower() == 'b':
            restaurants = add_restaurant(restaurants)

        elif user_choice.lower() == 'c':
            restaurants = edit_rating_rand(restaurants)

        elif user_choice.lower() == 'd':
            restaurants = edit_rating(restaurants)

        else:
            print "Please enter a letter from the menu."

start_restaurant_rater()