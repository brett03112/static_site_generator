import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    """
    Unit tests for the HTMLNode class.

    This test suite verifies the initialization, representation, and HTML property
    conversion functionality of the HTMLNode class.

    Test Coverage:
        - Initialization with various parameter combinations
        - props_to_html() method with different property configurations
        - __repr__() method output formatting
        - to_html() method NotImplementedError behavior
    """
    def test_init_with_all_parameters(self):
        node = HTMLNode("div", "Hello", None, {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertIsNone(node.children)
        self.assertEqual(node.props, {"class": "container"})

    def test_init_with_no_parameters(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_init_with_partial_parameters(self):
        node = HTMLNode(tag="p", value="Paragraph text")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Paragraph text")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props_to_html_with_single_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com"')

    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertIn('href="https://www.google.com"', result)
        self.assertIn('target="_blank"', result)

    def test_props_to_html_with_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_empty_dict(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_special_characters(self):
        node = HTMLNode(props={"data-value": "test&value", "id": "main-div"})
        result = node.props_to_html()
        self.assertIn('data-value="test&value"', result)
        self.assertIn('id="main-div"', result)

    def test_repr_with_all_parameters(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://example.com"})
        expected = "HTMLNode(a, Click me, None, {'href': 'https://example.com'})"
        self.assertEqual(repr(node), expected)

    def test_repr_with_no_parameters(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode(None, None, None, None)")

    def test_repr_with_children(self):
        child = HTMLNode("span", "child text")
        parent = HTMLNode("div", None, child)
        result = repr(parent)
        self.assertIn("HTMLNode(div, None,", result)
        self.assertIn("HTMLNode(span, child text, None, None)", result)

    def test_to_html_raises_not_implemented(self):
        node = HTMLNode("div", "test")
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
class TestLeafNode(unittest.TestCase):
    """
    Test suite for the LeafNode class.
    This test class validates the initialization and HTML rendering behavior of LeafNode instances,
    which represent leaf nodes in an HTML document tree (nodes without children).
    Tests:
        test_leafnode_init_with_all_parameters: Verifies LeafNode initialization with tag, value, and props.
        test_leafnode_init_with_no_parameters: Verifies LeafNode initialization with default None values.
        test_leafnode_init_with_partial_parameters: Verifies LeafNode initialization with only a tag parameter.
        test_leaf_to_html_p: Verifies that a LeafNode with a 'p' tag correctly renders to HTML string.
    """
    def test_leafnode_init_with_all_parameters(self):
        leaf = LeafNode("img", None, {"src": "image.png"})
        self.assertEqual(leaf.tag, "img")
        self.assertIsNone(leaf.value)
        self.assertIsNone(leaf.children)
        self.assertEqual(leaf.props, {"src": "image.png"})

    def test_leafnode_init_with_no_parameters(self):
        leaf = LeafNode()
        self.assertIsNone(leaf.tag)
        self.assertIsNone(leaf.value)
        self.assertIsNone(leaf.children)
        self.assertIsNone(leaf.props)

    def test_leafnode_init_with_partial_parameters(self):
        leaf = LeafNode(tag="br")
        self.assertEqual(leaf.tag, "br")
        self.assertIsNone(leaf.value)
        self.assertIsNone(leaf.children)
        self.assertIsNone(leaf.props)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just plain text")
        self.assertEqual(node.to_html(), "Just plain text")
    
    def test_leaf_to_html_no_value_raises_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Inline text")
        self.assertEqual(node.to_html(), "<span>Inline text</span>")
    
    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Main Heading")
        self.assertEqual(node.to_html(), "<h1>Main Heading</h1>")
    
    def test_leaf_to_html_with_multiple_props(self):
        node = LeafNode("a", "Link", {"href": "https://example.com", "target": "_blank"})
        result = node.to_html()
        self.assertIn('<a', result)
        self.assertIn('href="https://example.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertIn('>Link</a>', result)


if __name__ == "__main__":
    unittest.main()
