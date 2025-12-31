from block_md import *
from htmlnode import LeafNode
from textnode import *


def main():
    markdown = """
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

    node = markdown_to_html_node(markdown)

    # print(node)
    # if node.children:
    #     for child in node.children:
    #         print(child)
    #         print("\n")
    print(node.to_html())

    # a_node = ParentNode("p", [LeafNode("a", "link", {"href": "somewhere"})])
    # img_node = ParentNode(
    #     "p", [LeafNode("img", "", {"src": "something", "alt": "image"})]
    # )

    # print(a_node.to_html())
    # print(img_node.to_html())


if __name__ == "__main__":
    main()
