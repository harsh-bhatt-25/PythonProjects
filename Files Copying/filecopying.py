import os
import shutil

src_dir = r"C:\Users"
dst_dir = r"C:\Users"
for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith('.mp4'):
            fileName = os.path.join(root, file)
            shutil.copy(fileName, dst_dir)