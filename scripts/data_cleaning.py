#data cleaning 
import pandas as pd
import numpy as np
from datetime import datetime

# Load the dataset
patient_data = pd.read_csv('datasets/raw/PatientInfo.csv')
# Making a copy of the patient_data .csv file
patient_data_original = patient_data.copy()

# Shows the data shape
print(f"Original shape: {patient_data.shape}")

# Drop the columns with more than 50% missing values
columns_to_drop = ['contact_number', 'symptom_onset_date', 'deceased_date']
patient_data.drop = patient_data.drop(columns=columns_to_drop)

# Handling categorical missing values and filling them with 'Unknown'
patient_data['sex'] = patient_data['sex'].fillna('Unknown')
patient_data['infection_case'] = patient_data['infection_case'].fillna('Unknown')
patient_data['city'] = patient_data['city'].fillna('Unknown')

print(patient_data['age'].describe())

print(patient_data['age'].unique())

# converting the age column to numberic values. 
def clean_age(age_value):
    if pd.isna(age_value):
        return np.nan

    # return the age as is if its a number
    if isinstance(age_value, (int, float)):
        return age_value
    
    # this'll convert the string age ranges to numbers
    age_str = str(age_value).strip().lower()

    # to remove the 's' at the end of the age ranges in the column
    if age_str.endswith('s') and age_str[:-1].isdigit():
        return int(age_str[:-1]) # this will take the first digit of the range

    try:
        return int(age_str)
    except:
        return np.nan

# Applying the clean_age function to the age column
patient_data['age_int'] = patient_data['age'].apply(clean_age)

# Checking the median age
median_age = patient_data['age_int'].median()
print(f"Median age: {median_age}")

# Filling the missing ages with the median age
patient_data['age_int'] = patient_data['age_int'].fillna(median_age)

# Keep the original age column for reference
patient_data['age_original'] = patient_data['age']
patient_data['age'] = patient_data['age_int']

# Convert the dates to datetime objects
date_columns = ['confirmed_date', 'released_date']
for col in date_columns:
    if col in patient_data.columns:
        # cpverting to datetime and the errors='coerce' will set invalid dates to NaT
        patient_data[col] = pd.to_datetime(patient_data[col], errors='coerce')

# Checking the shape after cleaning
print(f"Shape after initial cleaning: {patient_data.shape}")

# Saved the cleaned data to a new csv file in processed folder
patient_data.to_csv('datasets/processed/PatientInfo_cleaned.csv', index=False)
