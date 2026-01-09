import os
from pathlib import Path

from block_md import markdown_to_blocks, markdown_to_html_node


def generate_pages_r(basepath, src_path, template_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    for item in os.listdir(src_path):
        new_src_path = os.path.join(src_path, item)

        if os.path.isfile(new_src_path):
            file_obj = Path(new_src_path)
            file_name = file_obj.stem
            new_dest_path = Path(dest_path) / f"{file_name}.html"
            generate_page(basepath, new_src_path, template_path, new_dest_path)
        else:
            new_dest_path = os.path.join(dest_path, item)
            generate_pages_r(basepath, new_src_path, template_path, new_dest_path)


def generate_page(basepath, src_path, template_path, dest_path):
    print(f'* src:"{src_path}" temp:"{template_path}" -> dest:"{dest_path}"')

    # read src and template files
    with open(src_path, "r") as src_file:
        md = src_file.read()

    with open(template_path, "r") as temp_file:
        template = temp_file.read()

    # Get title and html content
    title = extract_title(md)
    html_content = markdown_to_html_node(md).to_html()

    # Substitute content into the template
    filled_template = template.replace("{{ Title }}", title)
    filled_template = filled_template.replace("{{ Content }}", html_content)
    filled_template = filled_template.replace('href="/', f'href="{basepath}')
    filled_template = filled_template.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as dest_file:
        dest_file.write(filled_template)


def extract_title(markdown):
    title = markdown.split("\n\n")[0]
    if not title.startswith("# "):
        raise Exception("No title present")
    return title.replace("#", "").strip()
