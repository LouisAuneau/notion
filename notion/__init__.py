from notion.client import Client
from notion.services.databases import Databases

class Notion:

    def __init__(self, auth: str):
        """Constructor for Typeform API client"""
        client = Client(auth=auth)
        self.__databases = Databases(client)

    @property
    def databases(self) -> Databases:
        return self.__databases