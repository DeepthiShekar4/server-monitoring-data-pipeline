import pandas as pd

# Load dataset
df = pd.read_csv("data/Sample_Data_Ingestion.csv")

print("Dataset loaded successfully!")

# Convert timestamp column to datetime
df["Log_Timestamp"] = pd.to_datetime(df["Log_Timestamp"], dayfirst=True)

print("Timestamp converted!")

# Create Total Network Traffic column
df["Total_Network_Traffic"] = (
    df["Network_Traffic_In (MB/s)"] +
    df["Network_Traffic_Out (MB/s)"]
)

print("Total network traffic calculated!")

# Create Server Health Score
df["Health_Score"] = 100 - (
    (df["CPU_Utilization (%)"] +
     df["Memory_Usage (%)"] +
     df["Disk_IO (%)"]) / 3
)

print("Health score created!")

# Detect critical servers
df["Server_Status"] = df.apply(
    lambda row: "Critical"
    if row["CPU_Utilization (%)"] > 90 or row["Memory_Usage (%)"] > 90
    else "Normal",
    axis=1
)

print("Server status classification complete!")

# Save processed dataset
df.to_csv("output/processed_server_data.csv", index=False)

print("Processed dataset saved to output folder!")