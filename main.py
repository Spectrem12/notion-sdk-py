import yaml
from notion_client import *
import notion_client.lib as lib
import sys
import logging
from autologging import logged, traced, TRACE

logging.basicConfig(level = TRACE, stream = sys.stdout, format = "%(levelname)s:%(name)s:%(funcName)s:%(message)s")

@logged
@traced
class Notion_Sync():
    def __init__(self, ):
        self.databases  = {}
        self.client = self.get_connection()

    @logged
    def get_connection(self):
        # NOTION_TOKEN = os.getenv("NOTION_TOKEN", "")
        with open('Notion_Config.YAML') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            print(data)
        NOTION_TOKEN = data["Token"]

        while NOTION_TOKEN == "":
            print("NOTION_TOKEN not found.")
            NOTION_TOKEN = input("Enter your integration token: ").strip()

        return Client(auth=NOTION_TOKEN)

    @logged
    def get_db(self):
        results = self.client.databases.list()
        print("Listing databases: ")
        for item in results["results"]:
            test = lib.Database(**item)
            self.databases.update({item["title"][0]["plain_text"]:lib.Database(**item)})
            print(item["title"][0]["plain_text"])


    def query_db(self, database_name):
        db = self.databases[database_name]
        results = self.client.databases.query(database_id=db.id)
        db.get_pages(results["results"])

    def print_db(self):
        for page in self.databases["Tasks"].pages.items():
            print(page[1].title)


if __name__ == '__main__':
    logging.getLogger().setLevel(TRACE)
    notion = Notion_Sync()
    notion.get_connection()
    notion.get_db()
    notion.query_db("Tasks")
    notion.print_db()
