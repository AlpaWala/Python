import os
import shutil

files = os.listdir()

folders = ["PDFs", "Images", "TextFiles", "Videos"]

for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)

for file in files:
    if os.path.isfile(file):

        if file.endswith(".pdf"):
            shutil.move(file, "PDFs")

        elif file.endswith(".txt"):
            shutil.move(file, "TextFiles")

        elif file.endswith(".jpg") or file.endswith(".png"):
            shutil.move(file, "Images")

        elif file.endswith(".mp4"):
            shutil.move(file, "Videos")