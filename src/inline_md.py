import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        
        split_nodes = []
        if node.text.count(delimiter) % 2 != 0:
            raise ValueError("Invalid markdown")
        
        txts = node.text.split(delimiter)
        
        for i, txt in enumerate(txts):
            if txt == "":
                continue
            if i % 2 != 0:
                split_nodes.append(TextNode(txt, text_type))
            else:
                split_nodes.append(TextNode(txt, TextType.PLAIN_TEXT))
        new_nodes.extend(split_nodes)        
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]+)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pass