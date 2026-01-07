import os
import shutil

from copy_static import copy_files
from generate import generate_page

src_dir = "static"
dest_dir = "public"


def main():
    is_dest = os.path.exists(dest_dir)

    # delete existing destination
    if is_dest:
        shutil.rmtree(dest_dir)

    copy_files(src_dir, dest_dir)
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
