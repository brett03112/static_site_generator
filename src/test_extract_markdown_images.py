from textnode import TextNode, TextType
import unittest
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
