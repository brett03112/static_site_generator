from __future__ import annotations

class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: HTMLNode = None, props: dict = None):
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
    def __init__(self, tag: str = None, value: str = None, props: dict = None):
        """
        Initialize a LeafNode instance, which is a type of HTMLNode that does not have children.

        Args:
            tag (str, optional): The HTML tag name (e.g., 'p', 'a'). Defaults to None.
            value (str, optional): The text content/value of the HTML node. Defaults to None.
            props (dict, optional): A dictionary of HTML attributes (e.g., {'href': 'url'}). Defaults to None.
        """
        super().__init__(tag=tag, value=value, children=None, props=props)

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
