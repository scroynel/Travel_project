import requests


def fetch_place_from_api(external_id):
    link = f'https://api.artic.edu/api/v1/places/{external_id}'
    response = requests.get(link)
    return response.json()