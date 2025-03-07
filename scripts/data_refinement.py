import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Loading the processed data
processed_data = pd.read_csv('data/processed/patient_data_processed.csv')

# Creating age groups based on edpidemiological standards
def create_age_groups(age):
    if pd.isna(age):
        return 'Unknown'
    
    age_value = float(age)
    if age_value < 10:
        return '0-9'
    elif age_value < 20:
        return '10-19'
    elif age_value < 40:
        return '20-39'
    elif age_value < 60:
        return '40-59'
    elif age_value < 80:
        return '60-79'
    else:
        return '80+'
    
# Applying the create_age_groups function to the age column
processed_data['age_group'] = processed_data['age'].apply(create_age_groups)


# Check the distribution
age_distribution = processed_data['age_group'].value_counts(normalize=True) * 100
print(age_distribution)

# Calculating days to recovery
processed_data['days_to_recovery'] = (
    processed_data['released_date'] - processed_data['confirmed_date']
).dt.days

# Handle missing or negative values (data errors)
processed_data['days_to_recovery'] = processed_data['days_to_recovery'].apply(
    lambda x: x if (pd.notna(x) and x >= 0) else np.nan
)

# Checking the statistics of recovery time
print(processed_data['days_to_recovery'].describe())

# Handling the outliers 
plt.figure(figsize=(10,6))
sns.boxplot(data=processed_data, x='days_to_recovery')
plt.title('Boxplot of recovery time with potential outliers')
plt.savefig('recover_time_boxplot.png')
plt.close()

# Removing the outliers
mean_recovery = processed_data['days_to_recovery'].mean()
std_recovery = processed_data['days_to_recovery'].std()
upper_limit = mean_recovery + 3 * std_recovery

# Creating a capped version
processed_data['days_to_recovery_capped'] = processed_data['days_to_recovery'].apply(
    lambda x: min(x, upper_limit) if pd.notna(x) else np.nan
)

# Creating binary flags for analysis

