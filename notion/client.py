import json
import requests

from notion.constants import NOTION_API_HOSTNAME, NOTION_API_DEFAULT_VERSION, NOTION_API_VERSIONS
from notion.exception import NotionException

class Client():

    def __init__(self, auth: str, version: str = NOTION_API_DEFAULT_VERSION) -> None:
        self.auth = auth
        assert version in NOTION_API_VERSIONS, f"`version` must be one of {', '.join(NOTION_API_VERSIONS)}"
        self.version = version

    def request(self, method: str, url: str, data: dict = None) -> dict:
        headers = {
            'Authorization': 'Bearer ' + self.auth,
            'Content-Type': 'application/json',
            'Notion-Version': self.version
        }

        if data is not None:
            data = json.dumps(data)
        req = requests.Request(method, NOTION_API_HOSTNAME + url, headers=headers, data=data)
        prepped = req.prepare()
        resp = requests.Session().send(prepped)
        resp = resp.json()

        if resp['object'] == 'error':
            raise NotionException(code=resp['code'], status=resp['status'], message=resp['message'])
        else:
            return resp