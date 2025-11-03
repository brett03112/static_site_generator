from __future__ import annotations
from textnode import TextType

class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: HTMLNode = None, props: dict = None): # type: ignore
        """
        Initialize an HTMLNode instance.

        Args:
            tag (str, optional): The HTML tag name (e.g., 'div', 'p', 'a'). Defaults to None.
            value (str, optional): The text content/value of the HTML node. Defaults to None.
            children (HTMLNode, optional): Child HTMLNode(s) nested within this node. Defaults to None.
            props (dict, optional): A dictionary of HTML attributes (e.g., {'href': 'url', 'class': 'btn'}). Defaults to None.
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        """
        Converts the self.props dictionary to a string of HTML attributes.

        Expects self.props to be a dictionary of attribute-value pairs.
        If self.props is None or empty, returns an empty string.
        Example:
            If self.props is:
                {
                    "href": "https://www.google.com",
                    "target": "_blank",
                }
            then it returns:
                href="https://www.google.com" target="_blank"
        """
        b = ""
        if self.props:
            for key, value in self.props.items():
                a = f'{key}="{value}" '
                b += a
        return b.strip()

    def __repr__(self):
        """
        Return a string representation of the HTMLNode instance for debugging purposes.

        Returns:
            str: A string in the format "HTMLNode(tag, value, children, props)" where
                 tag is the HTML tag name, value is the node's text content, 
                 children is the list of child nodes, and props is the dictionary 
                 of HTML attributes.
        """
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict = None): # type: ignore
        """
        Initialize a LeafNode instance, which is a type of HTMLNode that does not have children.

        Args:
            tag (str, optional): The HTML tag name (e.g., 'p', 'a'). Defaults to None.
            value (str, optional): The text content/value of the HTML node. Defaults to None.
            props (dict, optional): A dictionary of HTML attributes (e.g., {'href': 'url'}). Defaults to None.
        """
        super().__init__(tag=tag, value=value, children=None, props=props) #type: ignore
    
    def to_html(self):
        """
        Convert the LeafNode instance to its HTML string representation.

        Returns:
            str: The HTML string representation of the LeafNode.
        
        Raises:
            ValueError: If the value is None (all leaf nodes must have a value).
        """
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        
        # If no tag, return raw text
        if self.tag is None:
            return self.value
        
        # Otherwise, render as HTML tag
        props_str = self.props_to_html()
        if props_str:
            return f"<{self.tag} {props_str}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag: str = None, children: list[HTMLNode] = None, props: dict = None): #type: ignore
        """
        Initialize a ParentNode instance, which is a type of HTMLNode that can have children.

        Args:
            tag (str, optional): The HTML tag name (e.g., 'div', 'ul'). Defaults to None.
            children (list[HTMLNode], optional): A list of child HTMLNode instances. Defaults to None.
            props (dict, optional): A dictionary of HTML attributes (e.g., {'class': 'container'}). Defaults to None.
        """
        super().__init__(tag=tag, value=None, children=children, props=props) #type: ignore

    def to_html(self):
        """
        Convert the ParentNode instance to its HTML string representation.

        Returns:
            str: The HTML string representation of the ParentNode.
        """
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        props_str = self.props_to_html()
        opening_tag = f"<{self.tag} {props_str}>" if props_str else f"<{self.tag}>"
        closing_tag = f"</{self.tag}>"

        children_html = ""
        if self.children:
            for child in self.children: #type: ignore
                children_html += child.to_html()

        return f"{opening_tag}{children_html}{closing_tag}"


def text_node_to_html_node(text_node):
    """
    Convert a TextNode instance to a LeafNode HTML representation.

    Args:
        text_node (TextNode): The TextNode instance to convert.

    Returns:
        LeafNode: The corresponding LeafNode representation of the TextNode.
    
    Raises:
        ValueError: If the text_node has an unsupported TextType or is an IMAGE type.
    """
    if text_node.text_type == TextType.PLAIN:
        return LeafNode(tag=None, value=text_node.text) #type: ignore
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.IMAGE:
        raise ValueError(f"IMAGE TextType is not supported for conversion to HTML node")
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")
