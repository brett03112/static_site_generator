import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    """
    Unit tests for the split_nodes_delimiter function.
    
    This test suite verifies the functionality of splitting text nodes based on
    delimiters to create inline markdown formatting (bold, italic, code).
    """
    
    def test_code_delimiter(self):
        """Test splitting with code delimiter (backtick)"""
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_bold_delimiter(self):
        """Test splitting with bold delimiter (**)"""
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_italic_delimiter(self):
        """Test splitting with italic delimiter (_)"""
        node = TextNode("This is text with an _italic phrase_ in the middle", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is text with an ", TextType.PLAIN),
            TextNode("italic phrase", TextType.ITALIC),
            TextNode(" in the middle", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_multiple_delimited_sections(self):
        """Test multiple delimited sections in one text node"""
        node = TextNode("This has `code` and `more code` blocks", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This has ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.PLAIN),
            TextNode("more code", TextType.CODE),
            TextNode(" blocks", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_non_plain_node_unchanged(self):
        """Test that non-PLAIN nodes are passed through unchanged"""
        node = TextNode("Already bold text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [node]
        self.assertEqual(new_nodes, expected)
    
    def test_multiple_nodes_mixed_types(self):
        """Test processing a list with mixed node types"""
        nodes = [
            TextNode("Plain text with `code`", TextType.PLAIN),
            TextNode("Already bold", TextType.BOLD),
            TextNode("More `code here`", TextType.PLAIN),
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [
            TextNode("Plain text with ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
            TextNode("Already bold", TextType.BOLD),
            TextNode("More ", TextType.PLAIN),
            TextNode("code here", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_no_delimiter_present(self):
        """Test text with no delimiter returns node unchanged"""
        node = TextNode("This text has no delimiters", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [node]
        self.assertEqual(new_nodes, expected)
    
    def test_unclosed_delimiter_raises_error(self):
        """Test that unclosed delimiter raises ValueError"""
        node = TextNode("This has an `unclosed delimiter", TextType.PLAIN)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertIn("Invalid markdown syntax", str(context.exception))
        self.assertIn("unclosed delimiter", str(context.exception))
    
    def test_delimiter_at_start(self):
        """Test delimiter at the start of text"""
        node = TextNode("`code` at the start", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("code", TextType.CODE),
            TextNode(" at the start", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_delimiter_at_end(self):
        """Test delimiter at the end of text"""
        node = TextNode("Text ending with `code`", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Text ending with ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_entire_text_delimited(self):
        """Test when entire text is delimited"""
        node = TextNode("`entire text is code`", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("entire text is code", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_empty_string_between_delimiters(self):
        """Test empty string between consecutive delimiters"""
        node = TextNode("Text with `` empty code", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Text with ", TextType.PLAIN),
            TextNode(" empty code", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_empty_list_input(self):
        """Test empty list returns empty list"""
        new_nodes = split_nodes_delimiter([], "`", TextType.CODE)
        self.assertEqual(new_nodes, [])
    
    def test_chaining_multiple_delimiters(self):
        """Test that the function can be chained for multiple delimiter types"""
        # First split on code
        node = TextNode("Text with `code` and **bold**", TextType.PLAIN)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        # Then split on bold
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("Text with ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
        ]
        self.assertEqual(nodes, expected)


if __name__ == "__main__":
    unittest.main()
