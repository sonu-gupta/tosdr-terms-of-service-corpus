# -*- coding: utf-8 -*-
import os
import shutil
from langdetect import detect
from bs4 import BeautifulSoup

# Define the directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
NON_ENGLISH_DIR = os.path.join(BASE_DIR, "non-english-documents")


# Loop over all the files in the data directory
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".html"):
        filepath = os.path.join(DATA_DIR, filename)
        try:
            # Parse the HTML with BeautifulSoup
            with open(filepath, "r", encoding="utf-8") as f:
                html = f.read()
            soup = BeautifulSoup(html, "html.parser")
            # Extract the text from the HTML
            text = soup.get_text()
            # Detect the language of the text
            language = detect(text)
            # Check if the language is English
            if language == "en":
                print(f"{filename} is in English.")
            else:
                # Create the non-English directory if it doesn't exist
                if not os.path.exists(NON_ENGLISH_DIR):
                    os.makedirs(NON_ENGLISH_DIR)
                # Move the file to the non-English directory
                shutil.move(filepath, os.path.join(NON_ENGLISH_DIR, filename))
                print(f"{filename} is in {language}. File moved to {NON_ENGLISH_DIR}.")
        except Exception as e:
            print(f"Error processing file {filename}: {e}")

