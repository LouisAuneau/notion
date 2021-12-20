class Emoji():
    """
    https://developers.notion.com/reference/emoji-object
    """

    def __init__(self, type: str = "emoji", emoji: str = None) -> None:
        self.type: str = type
        assert self.type == "emoji", "`type` of Emoji must be `emoji`"
        self.emoji: str = emoji