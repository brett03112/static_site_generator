import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    """
    Unit tests for the TextNode class.

    This test suite verifies the functionality of TextNode objects, including:
    - Equality comparison between TextNode instances
    - Inequality comparison for different text, types, and URLs
    - String representation (__repr__)
    - TextType enum values

    Test Cases:
        test_eq: Verifies that two TextNodes with identical text and type are equal.
        test_eq_with_url: Verifies equality when TextNodes include the same URL.
        test_not_eq_different_text: Verifies inequality when text content differs.
        test_not_eq_different_type: Verifies inequality when TextType differs.
        test_not_eq_different_url: Verifies inequality when URLs differ.
        test_not_eq_url_vs_none: Verifies inequality when one node has a URL and the other doesn't.
        test_eq_with_non_textnode: Verifies that a TextNode is not equal to non-TextNode objects.
        test_repr: Verifies the string representation of a TextNode with all parameters.
        test_repr_without_url: Verifies the string representation when URL is None.
        test_text_types: Verifies all TextType enum values are correct.
    """
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("Text 1", TextType.BOLD)
        node2 = TextNode("Text 2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_different_type(self):
        node = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_different_url(self):
        node = TextNode("Link", TextType.LINK, "https://example.com")
        node2 = TextNode("Link", TextType.LINK, "https://different.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_url_vs_none(self):
        node = TextNode("Text", TextType.PLAIN, "https://example.com")
        node2 = TextNode("Text", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_eq_with_non_textnode(self):
        node = TextNode("Text", TextType.PLAIN)
        self.assertNotEqual(node, "Not a TextNode")

    def test_repr(self):
        node = TextNode("Sample text", TextType.CODE, "https://example.com")
        expected = "TextNode(Sample text, TextType.CODE, https://example.com)"
        self.assertEqual(repr(node), expected)

    def test_repr_without_url(self):
        node = TextNode("Plain text", TextType.PLAIN)
        expected = "TextNode(Plain text, TextType.PLAIN, None)"
        self.assertEqual(repr(node), expected)

    def test_text_types(self):
        self.assertEqual(TextType.PLAIN.value, "plain")
        self.assertEqual(TextType.BOLD.value, "bold")
        self.assertEqual(TextType.ITALIC.value, "italic")
        self.assertEqual(TextType.CODE.value, "code")
        self.assertEqual(TextType.LINK.value, "link")
        self.assertEqual(TextType.IMAGE.value, "image")


if __name__ == "__main__":
    unittest.main()