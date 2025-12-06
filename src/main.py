from textnode import *
from htmlnode import LeafNode

def main():
    plain_node = TextNode("Winter is coming", TextType.PLAIN_TEXT)
    html_node = text_node_to_html_node(plain_node)
    print(html_node)
    
    

if __name__ == "__main__":
    main()
