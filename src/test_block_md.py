import unittest

from block_md import *

# temporary imports
# import unittest.util
# unittest.util._MAX_LENGTH = 10_000_000


class TestBlockMD(unittest.TestCase):
    def test_markdown_to_blocks1(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
        """

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
            ],
        )

    def test_markdown_to_blocks2(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_heading_block(self):
        blocks = [f"{'#' * i} Don't Panic!" for i in range(1, 7)]
        block_types = [block_to_block_type(block) for block in blocks]
        self.assertEqual(
            block_types,
            [
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
            ],
        )

    def test_block_to_code_block(self):
        blocks = [
            "```This is a string to test code blocks```",
            "```\nThis is another string to test code blocks as well\n```",
        ]
        block_types = [block_to_block_type(block) for block in blocks]
        self.assertEqual(block_types, [BlockType.CODE, BlockType.CODE])

    def test_block_to_quote_block(self):
        block = "> This is a block quote!"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_ulist_block(self):
        ulist_block = """- This is a list item
        - So is this
        - and this one as well"""
        block_type = block_to_block_type(ulist_block)
        self.assertEqual(block_type, BlockType.UL)

    def test_block_to_olist_block(self):
        olist_block = """1. This is a list item
        2. So is this
        3. and this one as well"""
        block_type = block_to_block_type(olist_block)
        self.assertEqual(block_type, BlockType.OL)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_multiblocks(self):
        md = """
# Header

Paragraph

- List item
- List item

1. ordered list item
2. ordered list item

[link](somewhere)

![image](something)

_italics_

**bold**

```
_Do_ or **do not**, there is no `try`
~ Master Yoda, Star wars
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>Header</h1><p>Paragraph</p><ul><li>List item</li><li>List item</li></ul><ol><li>ordered list item</li><li>ordered list item</li></ol><p><a href="somewhere">link</a></p><p><img src="something" alt="image"></img></p><p><i>italics</i></p><p><b>bold</b></p><pre><code>_Do_ or **do not**, there is no `try`\n~ Master Yoda, Star wars\n</code></pre></div>',
        )


if __name__ == "__main__":
    unittest.main()
