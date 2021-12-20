import datetime as dt
from typing import Dict, List, Union
from notion.models.rich_text import RichText
from notion.models.file import File
from notion.models.emoji import Emoji
from notion.models.property import Property


class Parent():
    """
    https://developers.notion.com/reference/database#page-parent
    """
    def __init__(self, type: str, page_id: str = None, workspace: str = None):
        self.type: str = type
        assert self.type in ['page_id', 'workspace']

        if self.type == 'page_id':
            assert page_id is not None, "`page_id` must be specified when `type` is `page_id`"
            self.page_id = page_id

        if self.type == 'workspace':
            assert workspace is not None, "`workspace` must be specified when `type` is `workspace`"
            self.workspace: str = workspace

class Database():
    """
    https://developers.notion.com/reference/database
    """

    def __init__(
        self, 
        object: str = 'database', 
        id: str = None, 
        created_time: str = None, 
        last_edited_time: str = None,
        title: List[Union[dict, RichText]] = None,
        parent: Union[dict, Parent] = None,
        icon: Union[dict, File, Emoji] = None,
        cover: Union[dict, File] = None,
        properties: Dict[str, Union[Property, dict]] = None,
        url: str = None
    ):
        self.object: str = object
        assert self.object == 'database'

        self.id: Union[str, None] = id

        if created_time is not None: 
            self.created_time: dt.datetime = dt.datetime.strptime(created_time, "%Y-%m-%dT%H:%M:%S.%f%z")
        else:
            self.created_time: None = None
        
        if last_edited_time is not None:
            self.last_edited_time: dt.datetime = dt.datetime.strptime(last_edited_time, "%Y-%m-%dT%H:%M:%S.%f%z")
        else:
            self.last_edited_time: None = None
        
        if title is not None:
            self.title: List[RichText] = [RichText(i) if isinstance(i, dict) else i for i in title]
        else:
            self.title = None
            
        self.parent: Union[None, Parent] = Parent(**parent)

        if isinstance(icon, dict):
            if icon['type'] == 'file':
                self.icon: File = File(**icon)
            elif icon['type'] == 'emoji':
                self.icon: Emoji = Emoji(**icon)
        elif isinstance(icon, File):
            self.icon: File = icon
        elif isinstance(icon, Emoji):
            self.icon: Emoji = icon
        else:
            self.icon = None

        self.cover: Union[File, None] = File(**cover) if isinstance(cover, dict) else cover

        if properties is not None:
            print(properties)
            self.properties: Dict[str, Property] = {k: (Property(**p) if isinstance(p, dict) else p) for k, p in properties.items()}

        if url is not None:
            self.url = url

        
                

