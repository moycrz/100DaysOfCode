import requests
from datetime import datetime
import os

USERNAME = "moy"
TOKEN = os.environ.get("AUTH_TOKEN")
GRAPH_ID = "graph1"
HEADER = {"X-USER-TOKEN": TOKEN, }

# TODO: Create account
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# TODO: Create a graph
# print(response.text)
graph_endpont = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

# response = requests.post(url=graph_endpont, json=graph_config, headers=headers)
# print(response.text)

# TODO: Post a Pixel
pixel_endopoin = f"{graph_endpont}/{GRAPH_ID}"

date = datetime.now().strftime('%Y%m%d')
pixel_config = {
    "date": date,
    "quantity": input("How long did you read today?(in minutes): "),
}

response = requests.post(url=pixel_endopoin, json=pixel_config, headers=HEADER)
print(response.text)

update_endpoint = f"{pixel_endopoin}/{date}"

update_config = {
    "quantity": "17",
}

# response = requests.put(url=update_endpoint, json=update_config, headers=HEADER)
# print(response.text)

delete_endpoin = f"{update_endpoint}"
#
# response = requests.delete(url=update_endpoint, headers=HEADER)
# print(response.text)

# TODO: Update Title

update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

update_graph_config = {
    "name": "Reading",
    "unit": "Minutes",
    "type": "int",
    "color": "momiji",
}

# response = requests.put(url=update_graph_endpoint, json=update_graph_config, headers=HEADER)
# print(response.text)
