import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    
    def test_ne(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)
    
    def test_ne2(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a text node2", TextType.PLAIN_TEXT)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.LINK_TEXT, "http://link_nodes.com")
        self.assertEqual(
            "TextNode(\"This is a text node\", link, \"http://link_nodes.com\")", repr(node)
        )

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("Winter is coming", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.value, "Winter is coming")
    
    def test_bold_text(self):
        node = TextNode("Hear me Roar", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.value, "Hear me Roar")
    
    def test_em_text(self):
        node = TextNode("Fire and Blood", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.value, "Fire and Blood")
        
    
    def test_code_text(self):
        node = TextNode("We Do Not Sow", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.value, "We Do Not Sow")
    
    def test_link_text(self):
        node = TextNode("Unbowed, Unbent, Unbroken", TextType.LINK_TEXT, "https://gotfandom/housemartel.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://gotfandom/housemartel.com"})
        self.assertEqual(html_node.value, "Unbowed, Unbent, Unbroken")
        
    
    def test_img(self):
        node = TextNode("golden rose on a green background", TextType.IMAGE_TEXT, "https://gotfandom/housetyrell/images/sigil.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://gotfandom/housetyrell/images/sigil.jpg", "alt": "golden rose on a green background"})
        self.assertEqual(html_node.value, None)   


if __name__ == "__main__":
    unittest.main()