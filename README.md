# Notion Python SDK

This python library allows you to interact with the official [Notion API](https://developers.notion.com/).

> ⚠️ It is under active development.

## Getting started

To install the library (it is not yet published):
```
pip install .
```

To use it:
```python
from notion import Notion

notion = Notion(token=<YOUR_NOTION_TOKEN>)
notion.databases.get(id=<DATABASE_ID>)
```