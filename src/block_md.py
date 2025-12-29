import re
from enum import Enum

from htmlnode import *
from inline_md import text_to_textnodes
from textnode import text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"


def markdown_to_html_node(markdown):
    html_nodes = []
    md_blocks = markdown_to_blocks(markdown)

    for block in md_blocks:
        # get the block type
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            match = re.match(r"^(#+)\s", block)
            if match:
                heading_text = re.sub(r"^#+\s*", "", block)
                hash_count = len(match.group(1))
                textnodes = text_to_textnodes(heading_text)  # a list of text nodes
                leafnodes = []  # create a list of leafnodes from textnodes
                for node in textnodes:
                    leafnodes.append(text_node_to_html_node(node))

                html_nodes.append(
                    ParentNode(f"h{hash_count}", leafnodes)
                )  # h{#} html parent node with the leafnodes as its children

        if block_type == BlockType.UL:
            pass

        if block_type == BlockType.OL:
            pass

        if block_type == BlockType.QUOTE:
            pass

        if block_type == BlockType.PARAGRAPH:
            pass

        if block_type == BlockType.CODE:
            pass

    return html_nodes


def markdown_to_blocks(markdown):
    blocks = [block.strip() for block in markdown.split("\n\n") if block != ""]
    return blocks


def block_to_block_type(block):
    if re.match(r"^#{1,6}\s.+", block):
        return BlockType.HEADING
    # elif re.match(r"^`{3}\n?.*\n?`{3}$", block):
    elif re.match(r"^`{3}|`{3}$", block):
        return BlockType.CODE
    elif re.match(r"^>\s.*", block):
        return BlockType.QUOTE
    elif re.match(r"^(-\s.*\n)+", block):
        return BlockType.UL
    elif re.match(r"^(\d+\.\s.*\n)+", block):
        return BlockType.OL
    else:
        return BlockType.PARAGRAPH
