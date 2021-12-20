from notion.client import Client
from notion.models.database import Database

class Databases():
    
    def __init__(self, client: Client):
        self._client = client

    def get(self, database_id: str) -> Database:
        return Database(**self._client.request('GET', f'/databases/{database_id}'))