import unittest

from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from htmlnode import text_node_to_html_node

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
        """
        The function `test_init_with_all_parameters` tests the initialization of an HTMLNode object with
        all parameters provided.
        """
        node = HTMLNode("div", "Hello", None, {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertIsNone(node.children)
        self.assertEqual(node.props, {"class": "container"})

    def test_init_with_no_parameters(self):
        """
        The function `test_init_with_no_parameters` initializes an `HTMLNode` object with no parameters
        and asserts that its attributes are all set to `None`.
        """
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
        """
        The function `test_props_to_html_with_single_prop` creates an HTML node with a single property
        and converts the property to HTML format.
        """
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com"')

    def test_props_to_html_with_multiple_props(self):
        """
        The function `test_props_to_html_with_multiple_props` tests the conversion of multiple
        properties of an HTML node to HTML attributes.
        """
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertIn('href="https://www.google.com"', result)
        self.assertIn('target="_blank"', result)

    def test_props_to_html_with_no_props(self):
        """
        The function `test_props_to_html_with_no_props` tests the `props_to_html` method of an
        `HTMLNode` object when no properties are present.
        """
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_empty_dict(self):
        """
        The function `test_props_to_html_with_empty_dict` creates an HTML node with an empty dictionary
        of properties and asserts that the properties are converted to an empty string in HTML format.
        """
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_special_characters(self):
        """
        The function `test_props_to_html_with_special_characters` tests the conversion of HTML node
        properties containing special characters to HTML attributes.
        """
        node = HTMLNode(props={"data-value": "test&value", "id": "main-div"})
        result = node.props_to_html()
        self.assertIn('data-value="test&value"', result)
        self.assertIn('id="main-div"', result)

    def test_repr_with_all_parameters(self):
        """
        The function `test_repr_with_all_parameters` tests the `repr` method of an `HTMLNode` object
        with all parameters specified.
        """
        node = HTMLNode("a", "Click me", None, {"href": "https://example.com"})
        expected = "HTMLNode(a, Click me, None, {'href': 'https://example.com'})"
        self.assertEqual(repr(node), expected)

    def test_repr_with_no_parameters(self):
        """
        The function `test_repr_with_no_parameters` tests the `repr` method of an `HTMLNode` object with
        no parameters.
        """
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode(None, None, None, None)")

    def test_repr_with_children(self):
        """
        The function `test_repr_with_children` creates a parent HTML node with a child node and tests
        the representation of the parent node.
        """
        child = HTMLNode("span", "child text")
        parent = HTMLNode("div", None, child)
        result = repr(parent)
        self.assertIn("HTMLNode(div, None,", result)
        self.assertIn("HTMLNode(span, child text, None, None)", result)

    def test_to_html_raises_not_implemented(self):
        """
        The function `test_to_html_raises_not_implemented` tests that calling the `to_html` method on an
        `HTMLNode` instance raises a `NotImplementedError`.
        """
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
        """
        The function `test_leafnode_init_with_all_parameters` tests the initialization of a LeafNode
        object with specified parameters.
        """
        leaf = LeafNode("img", None, {"src": "image.png"})
        self.assertEqual(leaf.tag, "img")
        self.assertIsNone(leaf.value)
        self.assertIsNone(leaf.children)
        self.assertEqual(leaf.props, {"src": "image.png"})

    def test_leafnode_init_with_no_parameters(self):
        """
        The function `test_leafnode_init_with_no_parameters` tests the initialization of a `LeafNode`
        object with no parameters.
        """
        leaf = LeafNode()
        self.assertIsNone(leaf.tag)
        self.assertIsNone(leaf.value)
        self.assertIsNone(leaf.children)
        self.assertIsNone(leaf.props)

    def test_leafnode_init_with_partial_parameters(self):
        """
        The function `test_leafnode_init_with_partial_parameters` tests the initialization of a LeafNode
        object with a specified tag and default values for other attributes.
        """
        leaf = LeafNode(tag="br")
        self.assertEqual(leaf.tag, "br")
        self.assertIsNone(leaf.value)
        self.assertIsNone(leaf.children)
        self.assertIsNone(leaf.props)
    
    def test_leaf_to_html_p(self):
        """
        The function `test_leaf_to_html_p` creates a `LeafNode` object with the tag "p" and content
        "Hello, world!", and then asserts that calling `to_html()` on the node returns "<p>Hello,
        world!</p>".
        """
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a_with_props(self):
        """
        The function creates an HTML `<a>` element with specified text content and properties.
        """
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_to_html_no_tag(self):
        """
        The function `test_leaf_to_html_no_tag` creates a `LeafNode` with plain text content and asserts
        that the HTML representation is the same as the plain text.
        """
        node = LeafNode(None, "Just plain text")
        self.assertEqual(node.to_html(), "Just plain text")
    
    def test_leaf_to_html_no_value_raises_error(self):
        """
        The function `test_leaf_to_html_no_value_raises_error` tests that a `ValueError` is raised when
        trying to convert a `LeafNode` with no value to HTML.
        """
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_to_html_span(self):
        """
        The function `test_leaf_to_html_span` creates a `LeafNode` object with the tag "span" and text
        "Inline text", then asserts that its HTML representation is "<span>Inline text</span>".
        """
        node = LeafNode("span", "Inline text")
        self.assertEqual(node.to_html(), "<span>Inline text</span>")
    
    def test_leaf_to_html_h1(self):
        """
        The function `test_leaf_to_html_h1` creates a `LeafNode` with "h1" tag and "Main Heading"
        content, then asserts that its HTML representation is "<h1>Main Heading</h1>".
        """
        node = LeafNode("h1", "Main Heading")
        self.assertEqual(node.to_html(), "<h1>Main Heading</h1>")
    
    def test_leaf_to_html_with_multiple_props(self):
        """
        The function `test_leaf_to_html_with_multiple_props` tests the conversion of a LeafNode object
        to HTML with multiple properties.
        """
        node = LeafNode("a", "Link", {"href": "https://example.com", "target": "_blank"})
        result = node.to_html()
        self.assertIn('<a', result)
        self.assertIn('href="https://example.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertIn('>Link</a>', result)

    # Tests for text_node_to_html_node function
    def test_text(self):
        """
        The function `test_text` creates a TextNode object with a specified text value and type,
        converts it to an HTML node, and then asserts the tag and value of the HTML node.
        """
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        """
        The `test_link` function tests the conversion of a TextNode with a link type to an HTML node
        with the correct tag, value, and properties.
        """
        node = TextNode("Google", TextType.LINK, url="https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Google")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})
    
    def test_bold(self):
        """
        The `test_bold` function tests the conversion of a TextNode with bold formatting to an HTML
        node.
        """
        node = TextNode("Bold Text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold Text")
    
    def test_italic(self):
        """
        The `test_italic` function tests the conversion of a TextNode with italic formatting to an HTML
        node.
        """
        node = TextNode("Italic Text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic Text")
    
    def test_code(self):
        """
        The function `test_code` creates a TextNode object with the text "Code Snippet" and text type
        CODE, then converts it to an HTML node and asserts its tag and value.
        """
        node = TextNode("Code Snippet", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code Snippet")

    def test_image(self):
        """
        The function `test_image` tests the conversion of a TextNode representing an image to an HTML
        node.
        """
        node = TextNode("Image", TextType.IMAGE, url="https://example.com/image.png")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_unsupported_text_type(self):
        """
        The function `test_unsupported_text_type` tests the conversion of a TextNode with an unsupported
        type to an HTML node.
        """
        node = TextNode("Unsupported", "UNSUPPORTED_TYPE")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

class TestParentNode(unittest.TestCase):
    """
    Test suite for the ParentNode class.
    This test class validates the initialization and HTML rendering behavior of ParentNode instances,
    which represent parent nodes in an HTML document tree (nodes that can have children).
    """
    def test_parentnode_init_with_all_parameters(self):
        """
        The function `test_parentnode_init_with_all_parameters` initializes a ParentNode object with
        specified parameters and asserts its properties.
        """
        child = LeafNode("span", "text")
        parent = ParentNode("div", [child], {"class": "container"})
        self.assertEqual(parent.tag, "div")
        self.assertIsNone(parent.value)
        self.assertEqual(len(parent.children), 1)
        self.assertEqual(parent.props, {"class": "container"})

    def test_parentnode_init_with_no_parameters(self):
        """
        The function `test_parentnode_init_with_no_parameters` tests the initialization of a
        `ParentNode` object with no parameters.
        """
        parent = ParentNode()
        self.assertIsNone(parent.tag)
        self.assertIsNone(parent.value)
        self.assertIsNone(parent.children)
        self.assertIsNone(parent.props)

    def test_parentnode_to_html_no_tag_raises_error(self):
        """
        The function tests that an error is raised when trying to convert a ParentNode to HTML without a
        tag.
        """
        child = LeafNode("p", "text")
        parent = ParentNode(None, [child])
        with self.assertRaises(ValueError, msg="ParentNode must have a tag"):
            parent.to_html()

    def test_parentnode_to_html_no_children_raises_error(self):
        """
        The function tests that a ParentNode without children raises a ValueError when converting to
        HTML.
        """
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError, msg="ParentNode must have children"):
            parent.to_html()

    def test_parentnode_to_html_with_props(self):
        """
        The function `test_parentnode_to_html_with_props` tests the conversion of a ParentNode object
        with specified properties to HTML format.
        """
        child = LeafNode("p", "Paragraph")
        parent = ParentNode("div", [child], {"id": "main", "class": "wrapper"})
        result = parent.to_html()
        self.assertIn('<div', result)
        self.assertIn('id="main"', result)
        self.assertIn('class="wrapper"', result)
        self.assertIn('<p>Paragraph</p>', result)
        self.assertIn('</div>', result)

    def test_parentnode_nested_structure(self):
        """
        The function creates a nested HTML structure with parent and child nodes containing text and
        formatting.
        """
        leaf1 = LeafNode("strong", "Bold")
        leaf2 = LeafNode("em", "Italic")
        child_parent = ParentNode("p", [leaf1, leaf2])
        parent = ParentNode("article", [child_parent])
        expected = "<article><p><strong>Bold</strong><em>Italic</em></p></article>"
        self.assertEqual(parent.to_html(), expected)

    def test_parentnode_deeply_nested(self):
        """
        The function `test_parentnode_deeply_nested` creates a nested structure of HTML elements and
        checks if the generated HTML string matches the expected output.
        """
        level3 = LeafNode("span", "deep")
        level2 = ParentNode("div", [level3])
        level1 = ParentNode("section", [level2])
        root = ParentNode("main", [level1])
        expected = "<main><section><div><span>deep</span></div></section></main>"
        self.assertEqual(root.to_html(), expected)

    def test_parentnode_mixed_children(self):
        """
        The function tests the creation of a parent node with mixed children in a tree structure and
        compares the generated HTML output with an expected value.
        """
        leaf = LeafNode("li", "Item 1")
        nested_parent = ParentNode("li", [LeafNode("strong", "Item 2")])
        parent = ParentNode("ul", [leaf, nested_parent])
        expected = "<ul><li>Item 1</li><li><strong>Item 2</strong></li></ul>"
        self.assertEqual(parent.to_html(), expected)

    def test_parentnode_with_text_only_children(self):
        """
        The function `test_parentnode_with_text_only_children` creates a parent node with two text-only
        children and tests if the HTML representation is as expected.
        """
        child1 = LeafNode(None, "Plain text 1")
        child2 = LeafNode(None, "Plain text 2")
        parent = ParentNode("p", [child1, child2])
        expected = "<p>Plain text 1Plain text 2</p>"
        self.assertEqual(parent.to_html(), expected)

    def test_parentnode_complex_props(self):
        """
        The function `test_parentnode_complex_props` creates a parent node with complex properties and
        checks if the generated HTML contains the expected attributes.
        """
        child = LeafNode("input", "", {"type": "text", "name": "username"})
        parent = ParentNode("form", [child], {"action": "/submit", "method": "POST"})
        result = parent.to_html()
        self.assertIn('<form', result)
        self.assertIn('action="/submit"', result)
        self.assertIn('method="POST"', result)
        self.assertIn('type="text"', result)
        self.assertIn('name="username"', result)

class TestHTMLNodeEdgeCases(unittest.TestCase):
    """
    Test suite for edge cases and boundary conditions in HTMLNode and its subclasses.
    """
    def test_leafnode_empty_string_value(self):
        """
        Test that a LeafNode with an empty string value renders correctly as an HTML element.

        Verifies that when a LeafNode is created with an empty string as its value,
        the to_html() method returns the appropriate opening and closing tags without
        any content between them.
        """
        node = LeafNode("div", "")
        self.assertEqual(node.to_html(), "<div></div>")

    def test_leafnode_with_quotes_in_value(self):
        """
        Test that a LeafNode correctly handles double quotes within its value.

        Verifies that when a LeafNode is created with text containing double quotes,
        the to_html() method preserves those quotes in the HTML output without
        escaping or modifying them.
        """
        node = LeafNode("p", 'He said "Hello"')
        self.assertEqual(node.to_html(), '<p>He said "Hello"</p>')

    def test_props_with_empty_string_value(self):
        """
        The function creates an HTML node with a property containing an empty string value and converts
        the properties to HTML format.
        """
        node = HTMLNode(props={"data-empty": ""})
        self.assertEqual(node.props_to_html(), 'data-empty=""')

    def test_parentnode_single_child(self):
        """
        The function creates a parent node with a single child node and tests if the HTML representation
        is correct.
        """
        child = LeafNode("span", "Only child")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span>Only child</span></div>")

    def test_parentnode_many_children(self):
        """
        The function tests a parent node with multiple children by creating a list of LeafNode objects
        and checking the generated HTML output.
        """
        children = [LeafNode("li", f"Item {i}") for i in range(5)]
        parent = ParentNode("ul", children)
        result = parent.to_html()
        self.assertTrue(result.startswith("<ul>"))
        self.assertTrue(result.endswith("</ul>"))
        for i in range(5):
            self.assertIn(f"<li>Item {i}</li>", result)

    def test_leafnode_special_html_chars_in_value(self):
        """
        The function `test_leafnode_special_html_chars_in_value` creates a `LeafNode` object with a
        value containing special HTML characters and checks if the resulting HTML output is as expected.
        """
        node = LeafNode("p", "<script>alert('xss')</script>")
        result = node.to_html()
        self.assertEqual(result, "<p><script>alert('xss')</script></p>")

    def test_props_ordering_consistency(self):
        """
        The function tests the consistency of the ordering of properties in an HTMLNode object.
        """
        props = {"z": "last", "a": "first", "m": "middle"}
        node = HTMLNode(props=props)
        result1 = node.props_to_html()
        result2 = node.props_to_html()
        self.assertEqual(result1, result2)

    

if __name__ == "__main__":
    unittest.main()
