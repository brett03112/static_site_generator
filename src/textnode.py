from enum import Enum

# The class `TextType` defines an enumeration for different types of text formatting options.
class TextType(Enum):
    """
    Enumeration of text node types for markdown parsing.

    This enum defines the different types of text formatting that can be
    represented in a text node. Each type corresponds to a specific markdown
    or HTML formatting style.

    Attributes:
        PLAIN (str): Plain text without any formatting.
        BOLD (str): Bold text formatting.
        ITALIC (str): Italic text formatting.
        CODE (str): Inline code formatting.
        LINK (str): Hyperlink text.
        IMAGE (str): Image reference.
    """
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

# The `TextNode` class represents a text node with specified text, text type, and optional URL.
class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        """
        Initialize a TextNode instance.

        Args:
            text (str): The text content of the node.
            text_type (TextType): The type of text formatting to apply.
            url (str, optional): The URL associated with the text node. Defaults to None.
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """
        Compare this TextNode with another object for equality.
        Two TextNode objects are considered equal if they have the same text content,
        text type, and URL.
        Args:
            other: The object to compare with this TextNode.
        Returns:
            bool: True if the other object is a TextNode with matching text, text_type,
                  and url attributes; False otherwise.
        """
        
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self):
        """
        Return a string representation of the TextNode instance for debugging.

        Returns:
            str: A string in the format "TextNode(text, text_type, url)" showing
                 the text content, text type, and URL of the TextNode.
        """
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
