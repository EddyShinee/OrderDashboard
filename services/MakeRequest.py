import requests


def MakeRequest(url, params=None, headers=None):
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response
    else:
        print("Failed to fetch data. Status code: ", response.status_code)
