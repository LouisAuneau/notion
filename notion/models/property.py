from typing import List, Union
from notion.models.annotations import Annotations
from notion.models.rich_text import RichText


class TitleConfiguration():
    """
    https://developers.notion.com/reference/database#title-configuration
    """
    pass

class TextConfiguration():
    """
    https://developers.notion.com/reference/database#title-configuration
    """
    pass


class NumberConfiguration():
    """
    https://developers.notion.com/reference/database#number-configuration
    """
    
    FORMATS = ["number", "number_with_commas", "percent", "dollar", "canadian_dollar", "euro", "pound", "yen", "ruble", "rupee", "won", "yuan", "real", "lira", "rupiah", "franc", "hong_kong_dollar", "new_zealand_dollar", "krona", "norwegian_krone", "mexican_peso", "rand", "new_taiwan_dollar", "danish_krone", "zloty", "baht", "forint", "koruna", "shekel", "chilean_peso", "philippine_peso", "dirham", "colombian_peso", "riyal", "ringgit", "leu", "argentine_peso", "uruguayan_peso"]

    def __init__(self, format: str = "number") -> None:
        assert format in NumberConfiguration.FORMATS, f"`format` must be one of {', '.join(NumberConfiguration.FORMATS)}"
        self.format = format
        

class SelectOption():
    """
    https://developers.notion.com/reference/database#select-options
    """

    COLORS = ["default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red"]

    def __init__(self, name: str = None, id: str = None, color: str = None) -> None:
        if id is not None:
            self.id = id

        if color is not None:
            assert color in SelectOption.COLORS, f"`color` must be one of {', '.join(SelectOption.COLORS)}"
            self.color = color

        if name is not None:
            self.name = name

class SelectConfiguration():
    """
    https://developers.notion.com/reference/database#select-configuration
    """

    def __init__(self, options: List[Union[dict, SelectOption]] = []) -> None:
        self.options = [SelectOption(**option) if isinstance(option, dict) else option for option in options]

class MultiSelectOption(SelectOption):
    """
    https://developers.notion.com/reference/database#multi-select-options
    """
    pass

class MultiSelectConfiguration():
    """
    https://developers.notion.com/reference/database#multi-select-configuration
    """

    def __init__(self, options: List[Union[dict, MultiSelectOption]] = []) -> None:
        self.options = [MultiSelectOption(**option) if isinstance(option, dict) else option for option in options]

class Property():
    """
    https://developers.notion.com/reference/database#property-object
    """

    TYPES = ["title", "rich_text", "number", "select", "multi_select", "date", "people", "files", "checkbox", "url", "email", "phone_number", "formula", "relation", "rollup", "created_time", "created_by", "last_edited_time", "last_edited_by"]

    def __init__(self, 
        id: str = None, 
        type: str = None, 
        name: str = None,
        title: Union[None, dict, TitleConfiguration] = None,
        rich_text: Union[None, dict, TextConfiguration] = None,
        number: Union[None, dict, NumberConfiguration] = None,
        select: Union[None, dict, SelectConfiguration] = None,
        multi_select: Union[None, dict, MultiSelectConfiguration] = None
    ) -> None:
        if id is not None:
            self.id = id

        if type is not None:
            assert type in Property.TYPES, f"`type` must be one of {', '.join(Property.property_types)}"
            self.type = type

        if name is not None:
            self.name = name

        if type == 'title':
            if title is None:
                raise ValueError("`title` must be specified when `type` is `title`")
            self.select = TitleConfiguration(**title) if isinstance(title, dict) else title

        if type == 'rich_text':
            if rich_text is None:
                raise ValueError("`rich_text` must be specified when `type` is `rich_text`")
            self.rich_text = TextConfiguration(**rich_text) if isinstance(rich_text, dict) else rich_text

        if type == 'number':
            if number is None:
                raise ValueError("`number` must be specified when `type` is `number`")
            self.number = NumberConfiguration(**number) if isinstance(number, dict) else number

        if type == 'select':
            if select is None:
                raise ValueError("`select` must be specified when `type` is `select`")
            self.select = SelectConfiguration(**select) if isinstance(select, dict) else select

        if type == 'multi_select':
            if multi_select is None:
                raise ValueError("`multi_select` must be specified when `type` is `multi_select`")
            self.multi_select = SelectConfiguration(**multi_select) if isinstance(multi_select, dict) else multi_select

        

