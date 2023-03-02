# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os

html_dir = "data/"
txt_dir = "text_files/"

for filename in os.listdir(html_dir):
    filepath = os.path.join(html_dir, filename)
    if os.path.getsize(filepath) < 2:
        # Skip the file if its size is less than 2B
        continue
    try:
        with open(filepath, "r", encoding="ISO-8859-1", errors="ignore") as f:
            html_text = f.read()
            soup = BeautifulSoup(html_text, "html.parser")
            text = soup.get_text()
            # Check if text contains more than 5 words
            if len(text.split()) > 5:
                with open(os.path.join(txt_dir, filename[:-5] + ".txt"), "w") as out:
                    out.write(text)
            else:
                print(f"File '{filename}' contains 5 or less words. Skipping...")
    except Exception as e:
        print(f"Error processing file '{filename}': {e}")
