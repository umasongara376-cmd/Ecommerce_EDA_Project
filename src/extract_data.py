import pandas as pd
from pathlib import Path
import urllib.request


# Official UCI dataset URL
url = "https://archive.ics.uci.edu/static/public/502/online+retail+ii.zip"

# File locations
raw_folder = Path("data/raw")
raw_folder.mkdir(parents=True, exist_ok=True)

zip_file = raw_folder / "online_retail_II.zip"


print("Downloading Online Retail II dataset...")

urllib.request.urlretrieve(url, zip_file)

print("Download completed!")
print("File saved at:", zip_file)