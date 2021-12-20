from typing import Union

from notion.models.annotations import Annotations


class RichText():
    """
    https://developers.notion.com/reference/rich-text
    """

    TYPES = ["text", "mention", "equation"]

    def __init__(self, plain_text: str = None, href: str = None, annotations: Union[dict, Annotations] = None, type: str = None) -> None:
        if plain_text is not None:
            self.plain_text = plain_text

        if href is not None:
            self.href = href
        
        if annotations is not None:
            self.annotations = Annotations(**annotations) if isinstance(annotations, dict) else annotations

        if type is not None:
            self.type = type
            assert type in RichText.TYPES, f"`type` must be one of {', '.join(RichText.types)}"