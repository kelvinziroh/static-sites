import os
import shutil
import sys

from copy_static import copy_files
from generate import generate_pages_r


def main():
    # capture base path
    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]

    # Copy, template, content generation src and dest directories
    cp_src = "./static"
    gen_src = "./content"
    template_src = "./template.html"
    dest = "./docs"

    # delete existing destination
    is_dest = os.path.exists(dest)
    if is_dest:
        shutil.rmtree(dest)

    # Recursively copy static files and directories to the public dir
    copy_files(cp_src, dest)

    # Recursively generate content to the public dir
    generate_pages_r(basepath, gen_src, template_src, dest)


if __name__ == "__main__":
    main()
