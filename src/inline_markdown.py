from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Split text nodes based on a delimiter, creating new nodes with different text types.
    
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
    
    for old_node in old_nodes:
        # If the node is not PLAIN text, add it as-is (no splitting needed)
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        
        # Split the text by the delimiter
        parts = old_node.text.split(delimiter)
        
        # If there's only one part, no delimiter was found
        if len(parts) == 1:
            new_nodes.append(old_node)
            continue
        
        # If there's an even number of parts, we have an unclosed delimiter
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid markdown syntax: unclosed delimiter '{delimiter}' in text: {old_node.text}")
        
        # Process the parts: even indices are plain text, odd indices are delimited text
        for i, part in enumerate(parts):
            # Skip empty strings
            if part == "":
                continue
                
            if i % 2 == 0:
                # Even index: plain text
                new_nodes.append(TextNode(part, TextType.PLAIN))
            else:
                # Odd index: delimited text (use the provided text_type)
                new_nodes.append(TextNode(part, text_type))
    
    return new_nodes
