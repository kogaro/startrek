import requests

# Define the BASE URL of the API here
API_BASEURL = "https://swapi.dev/api/"

# Returns the response JSON from a single API request
# Use only when no pagination is needed
def json_response(url):
    try:
        response = requests.get(url)
    except:
        exit("There was an error when connecting to the Star Wars API. Check API_BASEURL.")

    return response.json()

# Returns a full API request with handling pagination
def api_request(url):
    response = json_response(url)
    next_url = response["next"]
    result = response["results"]

    while next_url:
        response = json_response(next_url)
        result = result + response["results"]
        next_url = response["next"]

    return result

# Returns the list of films or a single film when the title is specified
def get_films(title = None):

    if title:
        return api_request(f"{API_BASEURL}/films/?search={title}")
    else:
        return api_request(f"{API_BASEURL}/films/")
    
# Returns the list of ships
def get_ships():

    return api_request(f"{API_BASEURL}/starships/")
    