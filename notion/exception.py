
class NotionException(Exception):
    """ Exception thrown by Notion API.

    See https://developers.notion.com/reference/errors.

    Attributes:
        status: Status code of the exception.
        code: Textual unique identifier.
        message: Human readable message.
    """
    def __init__(self, status, code, message):
        self.status = status
        self.code = code
        self.message = message
        super().__init__(self.message)