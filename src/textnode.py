from enum import Enum

# The class `TextType` defines an enumeration for different types of text formatting options.
class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

# The `TextNode` class represents a text node with specified text, text type, and optional URL.
class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """
        The function checks if two TextNode objects are equal based on their text, text type, and URL
        attributes.
        
        :param other: 
        The `other` parameter in the `__eq__` method is used to compare the current
        instance of a `TextNode` object with another object to check if they are equal. The method first
        checks if the `other` object is an instance of the `TextNode` class. If it is,

        :return: The `__eq__` method is being defined for a class (`TextNode`). This
        method is used to compare two instances of the class for equality.
        """
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self):
        """
        Summary:
            The `__repr__` function returns a string representation of a `TextNode` object with its text,
            text type, and URL.
        Returns:
            The `__repr__` method is returning a string representation of the object in the format
            "TextNode(text, text_type, url)". The values of `self.text`, `self.text_type`, and `self.url`
            will be inserted into the string when the method is called.
        """
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
