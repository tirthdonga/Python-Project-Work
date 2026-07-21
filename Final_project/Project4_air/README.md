<div align="center">

# 🌬️ Air Quality & Weather Monitor
### *Time-Series Analysis of Atmospheric Pollutants and Environmental Factors*

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Library-Seaborn-4C72B0?style=for-the-badge)
![Time Series](https://img.shields.io/badge/Concept-Time_Series-orange?style=for-the-badge)

</div>

---

# 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📁 Data Loading & Inspection](#-data-loading--inspection)
- [🧹 Time-Series Data Cleaning](#️-time-series-data-cleaning)
- [📉 Correlation Analysis](#-correlation-analysis)
- [📈 Weekly Trends Visualization](#-weekly-trends-visualization)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [👤 Author](#-author)

---

# 📌 Overview

**Air Quality & Weather Monitor** is a time-series data analysis project that processes sensor readings related to air pollution (CO, NOx, NO2) and weather conditions (Temperature, Humidity). Using **Pandas** for rigorous data wrangling and **Seaborn/Matplotlib** for visualization, the project explores the correlations between different atmospheric metrics and tracks pollutant levels over time.

---

# 🎯 Problem Statement

Raw sensor data often contains anomalies, missing values, and incorrect formats (e.g., specific error codes like -200). The goal is to clean this dataset, set a proper datetime index for time-series analysis, identify correlations between various pollutants and weather variables, and visualize long-term trends (like weekly Carbon Monoxide averages).

---

# ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📁 Data Ingestion | Loading raw air quality sensor data |
| 🧹 Anomaly Handling | Replacing error codes (`-200`) with `NaN` and dropping empty columns |
| ⏱️ Datetime Indexing | Combining Date and Time columns into a proper Pandas DatetimeIndex |
| 🧮 Missing Value Imputation | Filling missing data with numerical medians |
| 📉 Correlation Heatmap | Visualizing relationships between key variables (CO, NOx, Temp, Humidity) |
| 📈 Time-Series Resampling | Aggregating data by week (`resample('W')`) to plot long-term trends |

---

# 🏗️ Project Structure

```text
📦 Project4_air/
│── 📄 Air Quality.csv
│── 📄 air_quality_analysis.ipynb
└── 📄 README.md
```

---

# 🔄 Project Workflow

```text
Start
  │
  ▼
Load Data & Inspect Structure
  │
  ├── Drop Empty Columns & Rows
  ├── Handle Error Codes (-200 -> NaN)
  ├── Combine Date/Time into DatetimeIndex
  ├── Impute Missing Values (Median)
  ├── Select Key Variables & Generate Correlation Heatmap
  └── Resample Data Weekly & Plot CO Trends
```

---

# 📁 Data Loading & Inspection

- Load the `Air Quality.csv` dataset.
- The initial inspection reveals redundant unnamed columns, date/time split across two columns, and specific sensor values acting as error codes.

---

# 🧹 Time-Series Data Cleaning

- **Column Removal:** Drops entirely empty columns (`Unnamed: 15`, `Unnamed: 16`) and highly sparse columns like `NMHC(GT)`.
- **Anomaly Detection:** Replaces the sensor error code `-200` with `np.nan` to prevent skewed analysis.
- **Imputation:** Fills resulting `NaN` values with the median of each respective column.
- **Datetime Conversion:** Merges the `Date` and `Time` strings and converts them using `pd.to_datetime`. Sets this new `Datetime` column as the DataFrame index, enabling powerful time-series operations.

---

# 📉 Correlation Analysis

- Selects core variables: `CO(GT)`, `NOx(GT)`, `NO2(GT)`, `T` (Temperature), `RH` (Relative Humidity), and `AH` (Absolute Humidity).
- Generates a descriptive statistics summary.
- Creates a Seaborn heatmap to uncover correlations (e.g., how temperature or humidity correlates with pollutant concentration).

---

# 📈 Weekly Trends Visualization

- Utilizes Pandas' time-series capabilities to `.resample('W').mean()`, aggregating the hourly data into weekly averages.
- Plots the weekly average of Carbon Monoxide (`CO(GT)`) over time using a Matplotlib line chart, smoothing out daily noise to reveal broader environmental trends.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| 🐍 Python | Core Programming Language |
| 🐼 Pandas | Time-Series Indexing, Resampling & Cleaning |
| 🔢 NumPy | Handling `NaN` and numerical anomalies |
| 📉 Matplotlib | Line Plotting for Time Series |
| 📊 Seaborn | Statistical Heatmap Generation |

---

# 📈 Results & Insights

- ✅ Successfully transformed raw, messy sensor logs into a clean time-series format.
- ✅ Identified key relationships between different exhaust gases and weather metrics.
- ✅ Visualized the fluctuation of Carbon Monoxide levels over several months, allowing for pattern recognition (e.g., seasonal changes or policy impacts).

---

# 🏆 Advantages

| Advantage | Description |
|----------|-------------|
| ⏱️ Time-Series Ready | Robust conversion of string dates into a proper Pandas DatetimeIndex |
| 🛡️ Anomaly Safe | Explicitly handles hardware error codes (`-200`) before imputation |
| 📉 Trend Smoothing | Uses weekly resampling to provide a clearer, less noisy visualization |
| 🧹 Thorough Cleaning | Automatically drops empty rows/columns ensuring data integrity |

---

# 👤 Author

<div align="center">

# Tirth Donga

🎓 Python Air Quality Time-Series Project

---

### ⭐ Thank You For Visiting This Project ⭐

Made with ❤️ using Python, Pandas & Matplotlib

</div>
