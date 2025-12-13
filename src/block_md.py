import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = [
        block.strip() for block in markdown.split("\n\n") if block != ""
    ]
    return blocks

def block_to_block_type(block):
    if re.match(r"^#{1,6}\s.+", block):
        return BlockType.HEADING
    elif re.match(r"^`{3}\n?.*\n?`{3}$", block):
        return BlockType.CODE
    elif re.match(r">\s", block):
        return BlockType.QUOTE
    elif re.match(r"^(-\s.*\n)+", block):
        return BlockType.UL
    elif re.match(r"^(\d+\.\s.*\n)+", block):
        return BlockType.OL
    else:
        return BlockType.PARAGRAPH
