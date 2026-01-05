import os
import shutil


def copy_files(src, dest):
    is_src = os.path.exists(src)
    is_dest = os.path.exists(dest)

    if not is_src:
        raise Exception(f'Path "{src}" does not exist')

    # delete existing destination and create a new one
    if is_dest:
        shutil.rmtree(dest)
    os.mkdir(dest)

    # recursively copy files/directories from src to dest
    if os.path.isfile(src):  # base case
        shutil.copy(src, dest)
    else:  # recursive case
        src_items = os.listdir(src)
        for item in src_items:
            new_src = os.path.join(src, item)
            new_dest = os.path.join(dest, item)
            copy_files(new_src, new_dest)
