import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

files = [
    'datasets/Case.csv', 'datasets/PatientInfo.csv', 'datasets/Policy.csv', 'datasets/Region.csv', 'datasets/SearchTrend.csv', 'datasets/SeoulFloating.csv', 'datasets/Time.csv', 'datasets/TimeAge.csv', 'datasets/TimeGender.csv', 'datasets/TimeProvince.csv', 'datasets/Weather.csv'
]

# This function is to explore a dataframe
def explore_dataframe(df, file_name):
    print(f"\n{'='*50}")
    print(f"Exploring: {file_name}")
    print(f"{'='*50}")

    print(f"Shape of the dataframe: {df.shape} (rows, columns)")

    # The column names of the dataset
    print("`nColumns:")
    for col in df.columns:
        print(f"- {col}")

    
    # Displays information about the dataframe
    print("\nData types and missing values:")
    print(df.info())

    # This displays the first few rows of the csv file 
    print("\nFirst few rows:")
    print(df.head())

    # Percentage of missing values
    missing_values = df.isnull().sum()
    missing_percentage = (missing_values / len(df)) * 100
    print("\nMissing values:")
    for col, percentage in zip(df.columns, missing_percentage):
        if percentage > 0:
            print(f"- {col}: {percentage:.2f}%")

    print(f"\n{'='*50}\n")

# This will loop through the file to explore them

for file in files:
    try:
        df = pd.read_csv(file)
        explore_dataframe(df, file)
    except Exception as e:
        print(f"Error reading {file}: {e}")