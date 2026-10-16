# E-Commerce Exploratory Data Analysis

A Python-based exploratory data analysis (EDA) project built around the UCI **Online Retail II** dataset. The repository separates data acquisition and preparation scripts from Jupyter notebooks used for cleaning, analysis, and visualization.

## Project Structure

- `src/extract_data.py` — downloads the Online Retail II ZIP archive from the UCI Machine Learning Repository into `data/raw/`.
- `src/combine_data.py` — reads the two Excel sheets for 2009–2010 and 2010–2011, combines them into one table, saves a CSV, and prints basic data-quality checks.
- `notebooks/01_data_cleaning.ipynb` — notebook for data-cleaning work.
- `notebooks/02_eda_and_visualization.ipynb` — notebook for exploratory analysis and visualization.
- `data/raw/` — location used for downloaded and prepared raw data.

## Requirements

- Python 3.9 or later recommended
- pandas
- openpyxl (for reading Excel workbooks)
- Jupyter Notebook or JupyterLab
- Common plotting libraries may be required by the visualization notebook; install any additional packages imported by the notebook.

## Setup

1. Clone the repository and change into its directory.
2. Create and activate a virtual environment if desired.
3. Install the core dependencies:

   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate

   python -m pip install pandas openpyxl jupyter
   ```

4. Download the dataset:

   ```bash
   python src/extract_data.py
   ```

5. Extract the downloaded ZIP archive so that the Excel workbook is available at `data/raw/online_retail_II/online_retail_II.xlsx`. The current combination script expects this path.
6. Combine the two yearly sheets and run basic data-quality checks:

   ```bash
   python src/combine_data.py
   ```

7. Launch Jupyter and open the notebooks:

   ```bash
   jupyter notebook
   ```

## Data Source

The acquisition script uses the UCI Machine Learning Repository's Online Retail II dataset:

https://archive.ics.uci.edu/dataset/502/online+retail+ii

The data covers online retail transactions over two periods (2009–2010 and 2010–2011), which the combination script reads as separate Excel sheets before concatenating them.

## Current Workflow

1. Download the source archive.
2. Extract the Excel workbook into the expected folder.
3. Combine both year sheets into `data/raw/online_retail_raw.csv`.
4. Review missing values, duplicate rows, and data types in the script output.
5. Continue with the cleaning and EDA notebooks.

## Important Notes

- The extraction and combination scripts are separate steps; the current extraction script downloads the ZIP but does not unpack it automatically.
- Run commands from the repository root so relative paths resolve correctly.
- The data is downloaded from an external source, so internet access is needed for the download step.
- Analysis findings should be described only after executing the notebooks and verifying their outputs.

## License

No project-specific license is specified in this repository. Review the dataset's terms and contact the repository owner before redistributing project materials.