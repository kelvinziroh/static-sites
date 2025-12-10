import unittest

from inline_md import *
from textnode import *

class TestInlineMD(unittest.TestCase):
    def test_bold_md(self):
        node = TextNode("He leaned in close. **'Winter is coming'**, he said.", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertListEqual(
            new_nodes, 
            [
                TextNode("He leaned in close. ", TextType.PLAIN_TEXT),
                TextNode("'Winter is coming'", TextType.BOLD_TEXT),
                TextNode(", he said.", TextType.PLAIN_TEXT)
            ]
        )
    
    def test_italic_md(self):
        node = TextNode("He leaned in close. _'Winter is coming'_, he said.", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        self.assertListEqual(
            new_nodes, 
            [
                TextNode("He leaned in close. ", TextType.PLAIN_TEXT),
                TextNode("'Winter is coming'", TextType.ITALIC_TEXT),
                TextNode(", he said.", TextType.PLAIN_TEXT)
            ]
        )
    
    def test_code_md(self):
        node = TextNode("`Hello world`, are the first programming words for newbies", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertListEqual(
            new_nodes, 
            [
                TextNode("Hello world", TextType.CODE_TEXT),
                TextNode(", are the first programming words for newbies", TextType.PLAIN_TEXT)
            ]
        )
    
    def test_multiple_bold(self):
        node = TextNode("He stopped. **'Chaos isn't a pit'**, he said. **'Chaos is a ladder'**, he continued.", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertListEqual(
            new_nodes, 
            [
                TextNode("He stopped. ", TextType.PLAIN_TEXT),
                TextNode("'Chaos isn't a pit'", TextType.BOLD_TEXT),
                TextNode(", he said. ", TextType.PLAIN_TEXT),
                TextNode("'Chaos is a ladder'", TextType.BOLD_TEXT),
                TextNode(", he continued.", TextType.PLAIN_TEXT)
            ]
        )
    
    def test_multiple_italic(self):
        node = TextNode("He stopped. _'Chaos isn't a pit'_, he said. _'Chaos is a ladder'_, he continued.", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        self.assertListEqual(
            new_nodes, 
            [
                TextNode("He stopped. ", TextType.PLAIN_TEXT),
                TextNode("'Chaos isn't a pit'", TextType.ITALIC_TEXT),
                TextNode(", he said. ", TextType.PLAIN_TEXT),
                TextNode("'Chaos is a ladder'", TextType.ITALIC_TEXT),
                TextNode(", he continued.", TextType.PLAIN_TEXT)
            ]
        )

    def test_bold_italic(self):
        node = TextNode("He stopped. **'Chaos isn't a pit'**, he said. _'Chaos is a ladder'_, he continued.", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC_TEXT)
        self.assertListEqual(
            new_nodes, 
            [
                TextNode("He stopped. ", TextType.PLAIN_TEXT),
                TextNode("'Chaos isn't a pit'", TextType.BOLD_TEXT),
                TextNode(", he said. ", TextType.PLAIN_TEXT),
                TextNode("'Chaos is a ladder'", TextType.ITALIC_TEXT),
                TextNode(", he continued.", TextType.PLAIN_TEXT)
            ]
        )
    
    def test_extract_image(self):
        matches = extract_markdown_images(
            "House Targaryen: ![targaryen sigil](https://i.imgur.com/ji3Jlsa3.png)"
        )
        self.assertListEqual(
            matches,
            [("targaryen sigil", "https://i.imgur.com/ji3Jlsa3.png")]
        )
    
    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "House Targaryen: ![targaryen sigil](https://i.imgur.com/ji3Jlsa3.png) vs house Lannister: ![](https://i.imgur.com/mi3NlFa4.png)"
        )
        self.assertListEqual(
            matches,
            [("targaryen sigil", "https://i.imgur.com/ji3Jlsa3.png"), ("", "https://i.imgur.com/mi3NlFa4.png")]
        )
    
    def test_extract_images_only(self):
        matches = extract_markdown_images(
            "House Targaryen: ![targaryen sigil](https://i.imgur.com/ji3Jlsa3.png). [learn more](https://gotfandom/houses/sigils/targaryen.com)"
        )
        self.assertListEqual(
            matches,
            [("targaryen sigil", "https://i.imgur.com/ji3Jlsa3.png")]
        )

    def test_extract_links(self):
        pass
    
    def text_extract_multiple_links(self):
        pass
    
    def text_extract_links_only(self):
        pass