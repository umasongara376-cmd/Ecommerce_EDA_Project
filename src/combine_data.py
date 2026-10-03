import pandas as pd
from pathlib import Path


# Excel file location
excel_file = Path("data/raw/online_retail_II/online_retail_II.xlsx")

# Output folder
raw_folder = Path("data/raw")
raw_folder.mkdir(parents=True, exist_ok=True)


print("Reading Excel sheets...")

# Read both years
year_1 = pd.read_excel(
    excel_file,
    sheet_name="Year 2009-2010"
)

year_2 = pd.read_excel(
    excel_file,
    sheet_name="Year 2010-2011"
)


print("Year 2009-2010:", year_1.shape)
print("Year 2010-2011:", year_2.shape)


# Combine both years
df = pd.concat(
    [year_1, year_2],
    ignore_index=True
)


print("\nCombined data:", df.shape)


# Save raw combined data
output_file = raw_folder / "online_retail_raw.csv"

df.to_csv(
    output_file,
    index=False
)


print("\nRaw dataset saved successfully!")
print(output_file)


# Basic data-quality information
print("\n--- DATA QUALITY CHECK ---")

print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nData types:")
print(df.dtypes)