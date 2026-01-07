import os
import shutil


def copy_files(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
    # recursively copy files/directories from src to dest
    for item in os.listdir(src):
        new_src = os.path.join(src, item)
        new_dest = os.path.join(dest, item)

        if os.path.isfile(new_src):  # base case
            shutil.copy(new_src, new_dest)
        else:  # recursive case
            copy_files(new_src, new_dest)
