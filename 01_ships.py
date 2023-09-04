import starwars_api

FILM_TITLE = "Return of the Jedi"

print(f"Starships in movie: {FILM_TITLE}")

# Find the film with the title requested
films = starwars_api.get_films(FILM_TITLE)

# The should be only one movie with the specific title so we can look up the API starships from the first result
for starship_url in films[0]["starships"]:
    # The API returns the actual URLs so we can just iterate on those
    starship = starwars_api.json_response(starship_url)
    # Simply print the name of the ship from the response
    print(starship["name"])
