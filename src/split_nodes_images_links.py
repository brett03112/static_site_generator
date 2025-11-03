from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    """
    Splits TextNodes containing image markdown into separate TextNodes.
    
    Takes a list of TextNodes and splits any TEXT type nodes that contain
    image markdown syntax (![alt](url)) into multiple nodes:
    - TEXT nodes for plain text portions
    - IMAGE nodes for the images
    
    Args:
        old_nodes (list[TextNode]): List of TextNode objects to process
        
    Returns:
        list[TextNode]: New list with image markdown split into separate nodes
        
    Example:
        >>> node = TextNode("Text with ![img](url.png)", TextType.TEXT)
        >>> split_nodes_image([node])
        [
            TextNode("Text with ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "url.png")
        ]
    """
    new_nodes = []
    
    for node in old_nodes:
        # If not a PLAIN node, add it unchanged
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
            
        # Extract all images from the text
        images = extract_markdown_images(node.text)
        
        # If no images found, add the node unchanged
        if not images:
            new_nodes.append(node)
            continue
            
        # Process the text and split around images
        remaining_text = node.text
        
        for image_alt, image_url in images:
            # Split the text at the image markdown
            sections = remaining_text.split(f"![{image_alt}]({image_url})", 1)
            
            # Add the text before the image (if not empty)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
                
            # Add the image node
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            
            # Continue with the remaining text after the image
            remaining_text = sections[1] if len(sections) > 1 else ""
        
        # Add any remaining text after the last image (if not empty)
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.PLAIN))
    
    return new_nodes


def split_nodes_link(old_nodes):
    """
    Splits TextNodes containing link markdown into separate TextNodes.
    
    Takes a list of TextNodes and splits any TEXT type nodes that contain
    link markdown syntax ([text](url)) into multiple nodes:
    - TEXT nodes for plain text portions
    - LINK nodes for the links
    
    Args:
        old_nodes (list[TextNode]): List of TextNode objects to process
        
    Returns:
        list[TextNode]: New list with link markdown split into separate nodes
        
    Example:
        >>> node = TextNode("Text with [link](url.com)", TextType.TEXT)
        >>> split_nodes_link([node])
        [
            TextNode("Text with ", TextType.TEXT),
            TextNode("link", TextType.LINK, "url.com")
        ]
    """
    new_nodes = []
    
    for node in old_nodes:
        # If not a PLAIN node, add it unchanged
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
            
        # Extract all links from the text
        links = extract_markdown_links(node.text)
        
        # If no links found, add the node unchanged
        if not links:
            new_nodes.append(node)
            continue
            
        # Process the text and split around links
        remaining_text = node.text
        
        for link_text, link_url in links:
            # Split the text at the link markdown
            sections = remaining_text.split(f"[{link_text}]({link_url})", 1)
            
            # Add the text before the link (if not empty)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
                
            # Add the link node
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            
            # Continue with the remaining text after the link
            remaining_text = sections[1] if len(sections) > 1 else ""
        
        # Add any remaining text after the last link (if not empty)
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.PLAIN))
    
    return new_nodes
