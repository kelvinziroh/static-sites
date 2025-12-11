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
    
    def test_bold_only(self):
        node = TextNode("**'Winter is coming!'**", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("'Winter is coming!'", TextType.BOLD_TEXT)
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
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second image", TextType.IMAGE_TEXT, "https://i.imgur.com/3elNhQu.png"
                )
            ]
        )
    
    def test_split_images_beginning(self):
        node = TextNode(
            "![targaryen sigil](https://i.imgur.com/ji3Jlsa3.png): House Targaryen", TextType.PLAIN_TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("targaryen sigil", TextType.IMAGE_TEXT, "https://i.imgur.com/ji3Jlsa3.png"),
                TextNode(": House Targaryen", TextType.PLAIN_TEXT)
            ]
        )
    
    def test_split_images_end(self):
        node = TextNode(
            "House Targaryen: ![targaryen sigil](https://i.imgur.com/ji3Jlsa3.png)", TextType.PLAIN_TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("House Targaryen: ", TextType.PLAIN_TEXT),
                TextNode("targaryen sigil", TextType.IMAGE_TEXT, "https://i.imgur.com/ji3Jlsa3.png")
            ]
        )
        
    def test_split_image_only(self):
        node = TextNode("![targaryen sigil](https://i.imgur.com/ji3Jlsa3.png)", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("targaryen sigil", TextType.IMAGE_TEXT, "https://i.imgur.com/ji3Jlsa3.png")
            ]
        )
    
    def test_split_links(self):
        node = TextNode("House [Targaryen](https://gotfandom/houses/targaryen.com) has a sigil of three dragon heads", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("House ", TextType.PLAIN_TEXT),
                TextNode("Targaryen", TextType.LINK_TEXT, "https://gotfandom/houses/targaryen.com"),
                TextNode(" has a sigil of three dragon heads", TextType.PLAIN_TEXT)
            ]
        )

    def test_split_links_beginning(self):
        node = TextNode("[Targaryen](https://gotfandom/houses/targaryen.com) house with a sigil of three dragon heads", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("Targaryen", TextType.LINK_TEXT, "https://gotfandom/houses/targaryen.com"),
                TextNode(" house with a sigil of three dragon heads", TextType.PLAIN_TEXT)
            ]
        )
    
    def test_split_links_end(self):
        node = TextNode("House [Targaryen](https://gotfandom/houses/targaryen.com)", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("House ", TextType.PLAIN_TEXT),
                TextNode("Targaryen", TextType.LINK_TEXT, "https://gotfandom/houses/targaryen.com")
            ]
        )
    
    def test_split_links_only(self):
        node = TextNode("[House Targaryen](https://gotfandom/houses/targaryen.com)", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("House Targaryen", TextType.LINK_TEXT, "https://gotfandom/houses/targaryen.com")
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
        matches = extract_markdown_links(
            "House [Targaryen](https://gotfandom/houses/targaryen.com)"
        )
        self.assertListEqual(
            matches,
            [("Targaryen", "https://gotfandom/houses/targaryen.com")]
        )
    
    def text_extract_multiple_links(self):
        matches = extract_markdown_links(
            "Houses [Targaryen](https://gotfandom/houses/targaryen.com), [Martell](https://gotfandom/houses/martell.com) and [Dorn](https://https://gotfandom/houses/dorn.com)"
        )
        self.assertListEqual(
            matches,
            [("Targaryen", "https://gotfandom/houses/targaryen.com"), ("Martell", "https://gotfandom/houses/martell.com"), ("Dorn", "https://https://gotfandom/houses/dorn.com")]
        )
    
    def text_extract_links_only(self):
        matches = extract_markdown_images(
            "House Targaryen: ![targaryen sigil](https://i.imgur.com/ji3Jlsa3.png). [learn more](https://gotfandom/houses/sigils/targaryen.com)"
        )
        self.assertListEqual(
            matches,
            [("learn more", "https://gotfandom/houses/sigils/targaryen.com")]
        )