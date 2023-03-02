import os
import time
import requests
from bs4 import BeautifulSoup

# Define the URL and paths
URL = "https://edit.tosdr.org/documents"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Create the data directory if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Make the request to the URL and parse the HTML with BeautifulSoup
response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")
# Find the table with the services
table = soup.find("table")

# Loop through each row in the table (excluding the header row)
for row in table.find_all("tr")[1:]:
    try:
        # Extract the service name, service type, and URL
        columns = row.find_all("td")
        service_name = columns[0].text.strip()
        service_type = columns[1].text.strip()
        document_ = columns[1].find("a")["href"]
        doc_num = document_.split('/')[-1]
        url = URL+'/'+doc_num

        # Make the request to the service type URL and parse the HTML
        time.sleep(2)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the element with the "overflow" class and extract the HTML
        element = soup.find("div", {"class": "overflow"})
        html = element.text
        append_html_tags = "<html>"+html+"</html>"

        # Save the HTML to a file in the data directory
        filename = f"{service_name}_{service_type}.html"
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, "w") as f:
            f.write(html)

        print(f"Saved {filename} to {DATA_DIR}")

    except Exception as e:
        print(f"Error downloading {service_name} {service_type}: {e}")
