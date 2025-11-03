from textnode import TextNode, TextType
import re

def extract_markdown_images(text):
    """
    Create a function extract_markdown_images(text) that takes raw markdown text and returns a list of tuples. Each tuple should contain the alt text and the 
    URL of any markdown images. For example:

    ```python
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    ```
    """ 
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    """
    Create a function extract_markdown_links(text) that takes raw markdown text and returns a list of tuples. Each tuple should contain the link text and the 
    URL of any markdown links. For example:

    ```python
    text = "This is text with a [Google](https://www.google.com) link and a [GitHub](https://github.com) link."
    print(extract_markdown_links(text))
    # [("Google", "https://www.google.com"), ("GitHub", "https://github.com")]
    ```
    """ 
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches
