import os
import shutil

from copy_static import copy_files
from generate import generate_pages_r

src_dir = "static"
dest_dir = "public"


def main():
    is_dest = os.path.exists(dest_dir)

    # delete existing destination
    if is_dest:
        shutil.rmtree(dest_dir)

    # Recursively copy static files and directories to the public dir
    copy_files(src_dir, dest_dir)

    # Recursively generate content to the public dir
    generate_pages_r("content", "template.html", "public")


if __name__ == "__main__":
    main()
