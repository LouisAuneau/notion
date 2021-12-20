class Annotations():
    """
    https://developers.notion.com/reference/rich-text#annotations
    """

    possible_colors = ["default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red", "gray_background", "brown_background", "orange_background", "yellow_background", "green_background", "blue_background", "purple_background", "pink_background", "red_background"]

    def __init__(
        self, 
        bold: bool = False, 
        italic: bool = False, 
        strikethrough: bool = False, 
        underline: bool = False,    
        code: bool = False, 
        color: str = "default"
    ) -> None:
        self.bold = bold
        self.italic = italic
        self.strikethrough = strikethrough
        self.underline = underline
        self.code = code
        self.color = color