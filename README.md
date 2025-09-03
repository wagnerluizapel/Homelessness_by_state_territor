# Homelessness Rates by State/Territory in Australia

## Description
This project analyzes homelessness rates by state and territory in Australia from 2006 to 2021, using Python for data analysis and geospatial visualization.

## Structure
- `data/raw/Table_3_Rates_homelessness.csv`: Raw dataset containing homelessness rates by state/territory.
- `data/processed/gdf_merged.csv`: Processed dataset with merged homelessness rates and geospatial data.
- `data/processed/clean_csv.csv`: Cleaned and processed dataset.
- `notebooks/homelessnessByStateTerritory.ipynb`: Jupyter notebook for data cleaning, analysis, and merging with geospatial data.
- `streamlit/homelessnessByStateTerritory.py`: Streamlit application for interactive visualization of homelessness rates.
- `streamlit/requirements.txt`: List of Python dependencies required to run the project.
- `docs/README.md`: Project documentation (this file).

## Dataset Official URL
Site: https://www.abs.gov.au/statistics/people/housing/estimating-homelessness-census/2021

## How to Run
1. Navigate to the streamlit directory: `cd Homelessness_by_state_territor/streamlit/`.
2. Install the dependencies: `pip install -r requirements.txt`.
3. Run the dashboard: `streamlit run homelessnessByStateTerritory`.

- The dashboard will open in your default web browser at `http://localhost:8501`.

## Dependencies
The project requires the following Python libraries (listed in `requirements.txt`):
- `streamlit`
- `pandas`
- `matplotlib`
- `seaborn`
- `geopandas`
- `folium`
- `streamlit-folium`

To generate the `requirements.txt` file, run: pip freeze > requirements.txt

## Contact
Wagner Luiz Apel - 
wagnerapel@gmail.com
https://www.linkedin.com/in/wagner-luiz-apel/
https://github.com/wagnerluizapel

