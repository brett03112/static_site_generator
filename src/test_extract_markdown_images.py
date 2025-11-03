from testnode import TestNode, TextType
import unittest, re
from extract_markdown_images import extract_markdown_images, extract_markdown_links
    
class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.example.com)"
        )
        self.assertListEqual([("link", "https://www.example.com")], matches)
    
    def test_multiple_images_and_links(self):
        text = (
            "Here is an ![image1](https://i.imgur.com/image1.png) and a "
            "[link1](https://www.link1.com). Also, ![image2](https://i.imgur.com/image2.jpg) "
            "and [link2](https://www.link2.com)."
        )
        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)
        
        self.assertListEqual(
            [("image1", "https://i.imgur.com/image1.png"), ("image2", "https://i.imgur.com/image2.jpg")],
            image_matches
        )
        self.assertListEqual(
            [("link1", "https://www.link1.com"), ("link2", "https://www.link2.com")],
            link_matches
        )
        
if __name__ == '__main__':
    unittest.main()
    """
    This function processes a list of TextNode objects and splits any PLAIN text nodes
    that contain the specified delimiter. Text between delimiters is converted to the
    specified text_type, while text outside delimiters remains PLAIN.
    Args:
        old_nodes (list[TextNode]): List of TextNode objects to process
        delimiter (str): The delimiter string to split on (e.g., "`", "**", "_")
        text_type (TextType): The TextType to apply to text found between delimiters
    Returns:
        list[TextNode]: A new list of TextNode objects with delimited text split out
    Raises:
        ValueError: If a delimiter is opened but not closed (invalid markdown syntax)
    Examples:
        >>> node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        >>> new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        >>> # Returns: [
        >>>     TextNode("This is text with a ", TextType.PLAIN),
        >>>     TextNode("code block", TextType.CODE),
        >>>     TextNode(" word", TextType.PLAIN)
        >>> # ] 
    """
    new_nodes = []