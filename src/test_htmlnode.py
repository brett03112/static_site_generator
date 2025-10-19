import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()