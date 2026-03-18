import pandas as pd

# Load dataset
df = pd.read_csv("data/Sample_Data_Ingestion.csv")

# Show first rows
print("First 5 rows of the dataset:")
print(df.head())

# Show dataset info
print("\nDataset information:")
print(df.info())

# Show column names
print("\nColumn names:")
print(df.columns)