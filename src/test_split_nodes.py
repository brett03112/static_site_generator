import unittest
from textnode import TextNode, TextType
from split_nodes_images_links import split_nodes_image, split_nodes_link


class TestSplitNodesImage(unittest.TestCase):
    """
    Test suite for split_nodes_image function.
    """
    
    def test_split_images(self):
        """Test splitting a node with two images"""
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_single_image(self):
        """Test splitting a node with a single image"""
        node = TextNode(
            "Text before ![alt text](https://example.com/image.jpg) text after",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text before ", TextType.PLAIN),
                TextNode("alt text", TextType.IMAGE, "https://example.com/image.jpg"),
                TextNode(" text after", TextType.PLAIN),
            ],
            new_nodes,
        )
    
    def test_split_image_at_start(self):
        """Test image at the start of text"""
        node = TextNode(
            "![first](https://example.com/first.png) followed by text",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.IMAGE, "https://example.com/first.png"),
                TextNode(" followed by text", TextType.PLAIN),
            ],
            new_nodes,
        )
    
    def test_split_image_at_end(self):
        """Test image at the end of text"""
        node = TextNode(
            "Text before ![last](https://example.com/last.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text before ", TextType.PLAIN),
                TextNode("last", TextType.IMAGE, "https://example.com/last.png"),
            ],
            new_nodes,
        )
    
    def test_split_image_only(self):
        """Test node containing only an image"""
        node = TextNode(
            "![only image](https://example.com/only.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("only image", TextType.IMAGE, "https://example.com/only.png"),
            ],
            new_nodes,
        )
    
    def test_no_images(self):
        """Test node with no images returns original node"""
        node = TextNode("Just plain text with no images", TextType.PLAIN)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
    
    def test_non_text_node_unchanged(self):
        """Test that non-TEXT nodes pass through unchanged"""
        node = TextNode("Bold text", TextType.BOLD)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
    
    def test_multiple_nodes_mixed(self):
        """Test processing multiple nodes of mixed types"""
        nodes = [
            TextNode("Text with ![img](url.png)", TextType.PLAIN),
            TextNode("Bold text", TextType.BOLD),
            TextNode("More ![another](url2.png) text", TextType.PLAIN),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.PLAIN),
                TextNode("img", TextType.IMAGE, "url.png"),
                TextNode("Bold text", TextType.BOLD),
                TextNode("More ", TextType.PLAIN),
                TextNode("another", TextType.IMAGE, "url2.png"),
                TextNode(" text", TextType.PLAIN),
            ],
            new_nodes,
        )
    
    def test_empty_list(self):
        """Test empty list returns empty list"""
        new_nodes = split_nodes_image([])
        self.assertListEqual([], new_nodes)
    
    def test_adjacent_images(self):
        """Test adjacent images with no text between them"""
        node = TextNode(
            "![first](url1.png)![second](url2.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.IMAGE, "url1.png"),
                TextNode("second", TextType.IMAGE, "url2.png"),
            ],
            new_nodes,
        )
    
    def test_three_images(self):
        """Test splitting three images"""
        node = TextNode(
            "Start ![img1](url1.png) middle ![img2](url2.png) end ![img3](url3.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Start ", TextType.PLAIN),
                TextNode("img1", TextType.IMAGE, "url1.png"),
                TextNode(" middle ", TextType.PLAIN),
                TextNode("img2", TextType.IMAGE, "url2.png"),
                TextNode(" end ", TextType.PLAIN),
                TextNode("img3", TextType.IMAGE, "url3.png"),
            ],
            new_nodes,
        )
    
    def test_image_with_empty_alt_text(self):
        """Test image with empty alt text"""
        node = TextNode(
            "Text ![](https://example.com/image.png) more text",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text ", TextType.PLAIN),
                TextNode("", TextType.IMAGE, "https://example.com/image.png"),
                TextNode(" more text", TextType.PLAIN),
            ],
            new_nodes,
        )


class TestSplitNodesLink(unittest.TestCase):
    """
    Test suite for split_nodes_link function.
    """
    
    def test_split_links(self):
        """Test splitting a node with two links"""
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.PLAIN),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.PLAIN),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )
    
    def test_split_single_link(self):
        """Test splitting a node with a single link"""
        node = TextNode(
            "Text before [link text](https://example.com) text after",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text before ", TextType.PLAIN),
                TextNode("link text", TextType.LINK, "https://example.com"),
                TextNode(" text after", TextType.PLAIN),
            ],
            new_nodes,
        )
    
    def test_split_link_at_start(self):
        """Test link at the start of text"""
        node = TextNode(
            "[first link](https://example.com) followed by text",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("first link", TextType.LINK, "https://example.com"),
                TextNode(" followed by text", TextType.PLAIN),
            ],
            new_nodes,
        )
    
    def test_split_link_at_end(self):
        """Test link at the end of text"""
        node = TextNode(
            "Text before [last link](https://example.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text before ", TextType.PLAIN),
                TextNode("last link", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )
    
    def test_split_link_only(self):
        """Test node containing only a link"""
        node = TextNode(
            "[only link](https://example.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("only link", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )
    
    def test_no_links(self):
        """Test node with no links returns original node"""
        node = TextNode("Just plain text with no links", TextType.PLAIN)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)
    
    def test_non_text_node_unchanged(self):
        """Test that non-TEXT nodes pass through unchanged"""
        node = TextNode("Italic text", TextType.ITALIC)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)
    
    def test_multiple_nodes_mixed(self):
        """Test processing multiple nodes of mixed types"""
        nodes = [
            TextNode("Text with [link](url.com)", TextType.PLAIN),
            TextNode("Code text", TextType.CODE),
            TextNode("More [another](url2.com) text", TextType.PLAIN),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "url.com"),
                TextNode("Code text", TextType.CODE),
                TextNode("More ", TextType.PLAIN),
                TextNode("another", TextType.LINK, "url2.com"),
                TextNode(" text", TextType.PLAIN),
            ],
            new_nodes,
        )
    
    def test_empty_list(self):
        """Test empty list returns empty list"""
        new_nodes = split_nodes_link([])
        self.assertListEqual([], new_nodes)
    
    def test_adjacent_links(self):
        """Test adjacent links with no text between them"""
        node = TextNode(
            "[first](url1.com)[second](url2.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.LINK, "url1.com"),
                TextNode("second", TextType.LINK, "url2.com"),
            ],
            new_nodes,
        )
    
    def test_three_links(self):
        """Test splitting three links"""
        node = TextNode(
            "Start [link1](url1.com) middle [link2](url2.com) end [link3](url3.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Start ", TextType.PLAIN),
                TextNode("link1", TextType.LINK, "url1.com"),
                TextNode(" middle ", TextType.PLAIN),
                TextNode("link2", TextType.LINK, "url2.com"),
                TextNode(" end ", TextType.PLAIN),
                TextNode("link3", TextType.LINK, "url3.com"),
            ],
            new_nodes,
        )
    
    def test_link_does_not_match_image(self):
        """Test that links don't accidentally match image syntax"""
        node = TextNode(
            "This has an ![image](img.png) and a [link](url.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        # Should only split the link, not the image
        self.assertListEqual(
            [
                TextNode("This has an ![image](img.png) and a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "url.com"),
            ],
            new_nodes,
        )


class TestSplitNodesCombined(unittest.TestCase):
    """
    Test suite for using both split_nodes_image and split_nodes_link together.
    """
    
    def test_images_then_links(self):
        """Test processing images first, then links"""
        node = TextNode(
            "Text with ![img](img.png) and [link](url.com)",
            TextType.PLAIN,
        )
        # First split images
        nodes_after_images = split_nodes_image([node])
        # Then split links
        final_nodes = split_nodes_link(nodes_after_images)
        
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.PLAIN),
                TextNode("img", TextType.IMAGE, "img.png"),
                TextNode(" and ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "url.com"),
            ],
            final_nodes,
        )
    
    def test_links_then_images(self):
        """Test processing links first, then images"""
        node = TextNode(
            "Text with [link](url.com) and ![img](img.png)",
            TextType.PLAIN,
        )
        # First split links
        nodes_after_links = split_nodes_link([node])
        # Then split images
        final_nodes = split_nodes_image(nodes_after_links)
        
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "url.com"),
                TextNode(" and ", TextType.PLAIN),
                TextNode("img", TextType.IMAGE, "img.png"),
            ],
            final_nodes,
        )
    
    def test_mixed_complex(self):
        """Test complex text with multiple images and links"""
        node = TextNode(
            "Start ![img1](img1.png) then [link1](url1.com) middle ![img2](img2.png) and [link2](url2.com) end",
            TextType.PLAIN,
        )
        nodes_after_images = split_nodes_image([node])
        final_nodes = split_nodes_link(nodes_after_images)
        
        self.assertListEqual(
            [
                TextNode("Start ", TextType.PLAIN),
                TextNode("img1", TextType.IMAGE, "img1.png"),
                TextNode(" then ", TextType.PLAIN),
                TextNode("link1", TextType.LINK, "url1.com"),
                TextNode(" middle ", TextType.PLAIN),
                TextNode("img2", TextType.IMAGE, "img2.png"),
                TextNode(" and ", TextType.PLAIN),
                TextNode("link2", TextType.LINK, "url2.com"),
                TextNode(" end", TextType.PLAIN),
            ],
            final_nodes,
        )


if __name__ == "__main__":
    unittest.main()
