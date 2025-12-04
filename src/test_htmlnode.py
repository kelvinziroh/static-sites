import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(
            'a', 
            'Game of Thrones', 
            None, 
            {"href": "https://gotfandom.com", "target": "_blank"}
        )
        html_props = node.props_to_html()
        self.assertEqual(html_props, ' href="https://gotfandom.com" target="_blank"')
    
    def test_no_props(self):
        node = HTMLNode('p', 'Winter is coming', None, None)
        html_props = node.props_to_html()
        self.assertEqual(html_props, "")
    
    def test_repr(self):
        node = HTMLNode(
            'a', 
            'You know nothing Jon Snow', 
            None, 
            {"href": "https://gotfandom-characters-igrid.com"}
        )
        self.assertEqual(
            repr(node), 
            "HTMLNode(tag: a, value: You know nothing Jon Snow, children: None, props: {'href': 'https://gotfandom-characters-igrid.com'})"
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Winter is coming")
        self.assertEqual(node.to_html(), "<p>Winter is coming</p>")
        
    def test_leaf_to_html_rtxt(self):
        node = LeafNode(None, "Hear me roar")
        self.assertEqual(node.to_html(), "Hear me roar")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "King of the Andals", {"href": "https://gotfandom/salutation", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://gotfandom/salutation" target="_blank">King of the Andals</a>')


if __name__ == "__main__":
    unittest.main()