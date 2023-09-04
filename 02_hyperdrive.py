import starwars_api

MINIMUM_RATING = 1

print(f"Starships with hyperdrive rating >=1.0")

# Get the list of all ships from the API
ships = starwars_api.get_ships()

# Let's have a look at each ship and see it's rating
for ship in ships:
    # Let's try to convert the rating to float. For invalid values like "unkown" we will just use a 0 value.
    try:
        rating = float(ship["hyperdrive_rating"])
    except ValueError:
        rating = 0

    # Simply print the ships name and it's rating
    if rating >= MINIMUM_RATING:
        print(f"{ship['name']} ({rating})")