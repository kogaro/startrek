import starwars_api

CREW_MIN = 3
CREW_MAX = 100

print(f"Starships with crews between 3 and 100")

# Get the list of all ships from the API
ships = starwars_api.get_ships()

# Let's have a look at each ship and see it's crew compliment
for ship in ships:
    # Let's try to convert the crew size to int. For invalid values we will just use a 0 value as the exercise did not specify otherwise.
    try:
        crew = int(ship["crew"])
    except ValueError:
        crew = 0

    # Simply print the ships name and it's crew size
    if crew >= CREW_MIN and crew <= CREW_MAX:
        print(f"{ship['name']} ({crew})")