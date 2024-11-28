import modin.pandas as pd  # Use Modin for high-performance data handling
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:\\Users\\Purnapragya Sinha\\Downloads\\kaggg.csv"  # Replace with your dataset path
data = pd.read_csv(file_path)

# Data Overview
print("Data Head:\n", data.head())
print("\nData Info:\n")
data.info()

# Cleaning and Preprocessing
# Step 1: Handle missing values
print("\nChecking for missing values:\n", data.isnull().sum())
data.fillna(method='ffill', inplace=True)  # Forward fill for missing data

# Step 2: Convert columns if necessary
data['RecordID'] = data['RecordID'].astype(int)  # Ensure RecordID is integer

# Step 3: Create a new feature (e.g., PM10/PM2.5 ratio)
data['PM_Ratio'] = data['PM10'] / data['PM2_5']

# Data Analysis
# Example: Correlation analysis
correlation_matrix = data.corr()
print("\nCorrelation Matrix:\n", correlation_matrix)

# Example: Average AQI per HealthImpactClass
avg_aqi = data.groupby("HealthImpactClass")["AQI"].mean()
print("\nAverage AQI per HealthImpactClass:\n", avg_aqi)

# Data Visualization
# Plot 1: AQI Distribution
plt.figure(figsize=(10, 6))
plt.hist(data['AQI'], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of AQI", fontsize=16)
plt.xlabel("AQI", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.show()

# Plot 2: AQI vs Health Impact Score
plt.figure(figsize=(10, 6))
plt.scatter(data['AQI'], data['HealthImpactScore'], alpha=0.7, color='purple')
plt.title("AQI vs Health Impact Score", fontsize=16)
plt.xlabel("AQI", fontsize=12)
plt.ylabel("Health Impact Score", fontsize=12)
plt.grid(True)
plt.show()

# Plot 3: Average AQI per Health Impact Class
avg_aqi.plot(kind='bar', color='orange', figsize=(8, 5), edgecolor='black')
plt.title("Average AQI per Health Impact Class", fontsize=16)
plt.xlabel("Health Impact Class", fontsize=12)
plt.ylabel("Average AQI", fontsize=12)
plt.show()

# Aggregation Example
# Aggregating data by Temperature ranges
data['TemperatureRange'] = pd.cut(data['Temperature'], bins=[-10, 0, 10, 20, 30, 40], labels=["-10 to 0", "0 to 10", "10 to 20", "20 to 30", "30 to 40"])
agg_data = data.groupby('TemperatureRange')[['AQI', 'RespiratoryCases']].mean()
print("\nAggregated Data by Temperature Range:\n", agg_data)

# Save cleaned and analyzed data to a new CSV
data.to_csv("cleaned_air_quality_data_modin.csv", index=False)
print("\nCleaned and processed data saved to 'cleaned_air_quality_data_modin.csv'")
