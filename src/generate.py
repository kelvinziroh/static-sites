import os

from block_md import markdown_to_html_node


def extract_title(markdown):
    title = markdown.split("\n\n")[0]
    if not title.startswith("# "):
        raise Exception("No title present")
    return title.replace("#", "").strip()


def generate_page(from_path, template_path, dest_path):
    print(
        f'Generating page from "{from_path}" to "{dest_path}" using "{template_path}"'
    )

    # open and read the markdown file
    with open(from_path, "r") as file:
        md = file.read()

    html_content = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    # Fill in the template
    with open(template_path, "r") as rd_file:
        temp = rd_file.read()

    temp = temp.replace("{{ Title }}", title)
    temp = temp.replace("{{ Content }}", html_content)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as wt_file:
        wt_file.write(temp)
