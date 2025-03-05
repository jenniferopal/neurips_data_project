# COVID-19 Data Cleaning and Transformation Project

## Project Overview
This project focuses on cleaning, transforming, and analyzing the DS4C (Data Science for COVID-19) dataset from the NeurIPS 2020 competition available on Kaggle. The goal is to create a robust data pipeline that handles real-world messy data and prepares it for further analysis and visualization.

## Dataset Description
The DS4C dataset contains multiple CSV files with information about COVID-19 cases in South Korea:

- **Case.csv**: Case-specific information
- **PatientInfo.csv**: Demographic and clinical data about patients
- **Policy.csv**: Government policies implemented during the pandemic
- **Region.csv**: Regional information
- **SearchTrend.csv**: Search trend data related to COVID-19
- **SeoulFloating.csv**: Population movement data in Seoul
- **Time.csv**: Time-series data
- **TimeAge.csv**: Age-related time-series data
- **TimeGender.csv**: Gender-related time-series data
- **TimeProvince.csv**: Province-level time-series data
- **Weather.csv**: Weather information

## Project Structure
```
covid-data-project/
│
├── data/
│   ├── raw/                 # Original dataset files
│   └── processed/           # Cleaned and transformed data
│
├── notebooks/
│   ├── exploration.ipynb    # Initial data exploration
│   └── cleaning.ipynb       # Data cleaning process
│
├── scripts/
│   ├── data_exploration.py  # Functions for data exploration
│   ├── data_cleaning.py     # Functions for data cleaning
│   └── utils.py             # Utility functions
│
├── README.md                # Project documentation
└── requirements.txt         # Project dependencies
```

## Data Cleaning Approach
The data cleaning process follows these steps:

1. **Initial Exploration**: Understanding the structure, content, and quality of each dataset
2. **Missing Value Analysis**: Quantifying and addressing missing values based on their percentage and importance
3. **Data Type Correction**: Ensuring all columns have appropriate data types (dates, numbers, categories)
4. **Categorical Data Standardization**: Creating consistent categories and handling unknown values
5. **Temporal Data Processing**: Converting and aligning date/time information
6. **Outlier Detection and Handling**: Identifying and addressing statistical outliers
7. **Feature Engineering**: Creating new variables that might be useful for analysis
8. **Data Integration**: Connecting information across multiple files through key relationships

## Key Challenges
- **PatientInfo.csv** has significant missing data, particularly in:
  - `contact_number` (84.69%)
  - `symptom_onset_date` (86.64%)
  - `deceased_date` (98.72%)
  - `infected_by` (73.94%)
  - `released_date` (69.27%)
  - `age` (26.72%)
  - `sex` (21.72%)
  
- **Policy.csv** has missing data in:
  - `end_date` (60.66%)
  - `detail` (3.28%)

## Implementation Details
The data cleaning implementation uses:
- **pandas** for data manipulation
- **numpy** for numerical operations
- **matplotlib/seaborn** for data visualization

## Usage
1. Clone this repository
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the exploration script: `python scripts/data_exploration.py`
4. Run the cleaning script: `python scripts/data_cleaning.py`

## Future Work
- Develop a dashboard to visualize the cleaned data
- Perform time-series analysis on COVID-19 progression
- Analyze the effectiveness of different policies on case numbers
- Investigate demographic factors influencing COVID-19 outcomes