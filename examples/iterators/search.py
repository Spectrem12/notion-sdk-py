import os
import sys

from notion_client.client import Client
from notion_client.helpers import EndpointIterator

api_key = (
    os.getenv("NOTION_API_KEY") or "secret_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
)
client = Client(auth=api_key)

findme = sys.argv[1]

iter = EndpointIterator(
    endpoint=client.search,
    query=findme,
    sort={"direction": "ascending", "timestamp": "last_edited_time"},
)

n_items = 0

for item in iter:
    print(f'{item["object"]} => {item["id"]}')
    n_items += 1

print(f"total results: {n_items}")
