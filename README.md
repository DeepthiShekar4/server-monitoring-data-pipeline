# Server Monitoring Data Engineering Pipeline

## Project Overview
This project presents an end-to-end data engineering pipeline designed for monitoring and analyzing server performance. It demonstrates the complete workflow from raw data ingestion to data transformation and visualization, enabling actionable insights through a Power BI dashboard.

The solution focuses on building a structured, scalable, and efficient pipeline to convert raw system logs into meaningful performance indicators.

---

## Objectives
- Design and implement a robust data ingestion pipeline  
- Perform efficient data transformation and feature engineering  
- Generate key performance metrics for system monitoring  
- Develop an interactive dashboard for analytical insights  

---

## Technology Stack
- Python  
- Pandas  
- Power BI  
- Jupyter Notebook (.ipynb)  
- CSV Data Sources  
- Visual Studio Code  

---

## Data Pipeline Architecture
Raw Data → Data Ingestion → Data Transformation → Processed Data → Visualization Layer (Power BI)

---

## Project Structure
server-monitoring-data-pipeline/

│
├── data/                  # Raw dataset  
├── scripts/               # Data ingestion and transformation scripts  
│   ├── ingest_data.py  
│   └── transform_data.py  
│
├── output/                # Processed dataset  
│   └── processed_server_data.csv  
│
├── dashboard/             # Power BI dashboard  
│   └── Deepthi.pbix  
│
├── documentation/         # Project documentation  
│   └── Server_Monitoring_Data_Pipeline_Documentation.pptx  
│
├── notebook/              # Notebook implementation  
│   ├── ingest_data.ipynb  
│   └── transform_data.ipynb  
│
├── README.md  
└── requirements.txt  

---

## Data Processing Workflow

### Data Ingestion
- Extracted raw server log data from CSV sources  
- Loaded and structured data using Pandas for further processing  

### Data Transformation
- Standardized timestamp format for time-series analysis  
- Engineered new features for enhanced monitoring capabilities  
- Computed derived metrics including:

Total Network Traffic = Network_Traffic_In + Network_Traffic_Out  

Server Health Score = 100 - (CPU_Utilization + Memory_Usage + Disk_IO) / 3  

- Performed data cleaning and preprocessing for consistency and accuracy  

---

## Dashboard Preview

### Overview Dashboard
![Dashboard Overview](Dashboard_1.png)

### Network & Performance Analysis
![Network Analysis](Dashboard_2.png)

## Dashboard Capabilities

The Power BI dashboard provides a structured and interactive view of server performance metrics, focusing on the following key areas:

- **CPU Utilization Trend Analysis**  
  Visualizes CPU usage over time across multiple servers, enabling comparison of performance patterns and workload fluctuations.

- **Memory and Performance Metrics Tracking**  
  Displays trends of memory usage alongside CPU utilization and health score, supporting analysis of system performance behavior.

- **Network Traffic Analysis**  
  Represents average network traffic (inbound and outbound) across different servers, helping identify high-load systems and traffic distribution.

- **Server Health Score Monitoring**  
  Uses a gauge visual to indicate the average health score, providing a quick assessment of overall system stability.

- **Downtime and Operational Metrics**  
  Highlights total downtime and aggregated performance indicators for better operational visibility.

- **Server Status Distribution**  
  Displays the proportion of servers categorized as normal or critical using a donut chart for quick status assessment.

- **Geographical Performance Comparison**  
  Compares average health scores across server locations, enabling region-based performance evaluation.

- **Interactive Filtering and Drill-down**  
  Allows users to filter data by server location and analyze trends over time for deeper insights.

---

## Key Insights
- Identification of high resource utilization patterns  
- Detection of performance bottlenecks and system stress points  
- Improved visibility into server health and operational efficiency  

---

## Execution Steps

Install dependencies:
pip install -r requirements.txt  

Run data ingestion:
python scripts/ingest_data.py  

Run data transformation:
python scripts/transform_data.py  

---

## Future Enhancements
- Integration of real-time data streaming pipelines  
- Deployment on cloud platforms such as AWS, GCP, or Azure  
- Implementation of automated alerting mechanisms  
- Incorporation of machine learning models for anomaly detection  

---

## Author
Deepthi C Shekar  

---

## References
GitHub Repository: (add your repository link)  
