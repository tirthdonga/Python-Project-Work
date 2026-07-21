<div align="center">

# 🌍 COVID-19 Global Monitor
### *Data Analysis and Visualization of the COVID-19 Pandemic*

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Library-Seaborn-4C72B0?style=for-the-badge)
![Data Analysis](https://img.shields.io/badge/Concept-Data_Analysis-orange?style=for-the-badge)

</div>

---

# 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📁 Data Loading & Overview](#-data-loading--overview)
- [🧹 Data Cleaning](#️-data-cleaning)
- [📊 Visualizing Top Countries by Cases](#-visualizing-top-countries-by-cases)
- [📉 Descriptive Statistics & Correlation](#-descriptive-statistics--correlation)
- [📈 Visualizing Mortality Rate](#-visualizing-mortality-rate)
- [🌍 Regional Analysis](#-regional-analysis)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [👤 Author](#-author)

---

# 📌 Overview

**COVID-19 Global Monitor** is a data analysis project utilizing **Pandas**, **Matplotlib**, and **Seaborn** to explore global COVID-19 statistics. The project focuses on cleaning raw datasets, calculating key metrics like mortality and recovery rates, and visualizing the impact of the pandemic across different countries and continents.

---

# 🎯 Problem Statement

The goal of this project is to process and analyze raw COVID-19 data to extract meaningful insights. By handling missing values, calculating derived metrics, and creating clear visualizations, the project aims to identify the countries most affected by cases and mortality, as well as understand the distribution of the pandemic across continents.

---

# ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📁 Data Ingestion | Loading and inspecting raw COVID-19 CSV data |
| 🧹 Data Cleaning | Handling missing values and filtering out aggregate regions |
| 🧮 Metric Calculation | Deriving Mortality Rate and Recovery Rate |
| 📊 Case Visualizations | Identifying and charting the top 5 countries by total cases |
| 📉 Correlation Analysis | Generating correlation matrices for key numerical metrics |
| 💀 Mortality Analysis | Visualizing the top 5 countries by mortality rate (filtered for >10k cases) |
| 🌍 Continental Overview | Analyzing total cases and deaths aggregated by continent |

---

# 🏗️ Project Structure

```text
📦 Project1_covid 19/
│── 📄 covid_19.csv
│── 📄 covid_analysis.ipynb
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
  ├── Clean Data (Handle NaNs, Convert Dates)
  ├── Filter Data (Remove Aggregate Rows)
  ├── Top 5 Cases Visualization
  ├── Descriptive Stats & Correlation Heatmap
  ├── Calculate Rates (Mortality, Recovery)
  ├── Top 5 Mortality Visualization
  └── Continent Aggregation & Visualization
```

---

# 📁 Data Loading & Overview

- Load `covid_19.csv` using Pandas.
- Display the first few rows to understand the schema.
- Check data types and identify missing values using `.info()`.

---

# 🧹 Data Cleaning

- Fill missing numerical values (`Recovered`, `Deaths`, `Tests`) with `0`.
- Fill missing categorical values (`continent`) with `'Other'`.
- Convert the `day` column to datetime format.
- Remove aggregate rows (e.g., 'All', 'Europe', 'Asia') to isolate individual countries.
- Drop duplicate entries.

---

# 📊 Visualizing Top Countries by Cases

- Sort the cleaned dataset to find the top 5 countries with the highest total COVID-19 cases.
- Generate a Seaborn bar plot to visualize these countries.

---

# 📉 Descriptive Statistics & Correlation

- Generate descriptive statistics (`mean`, `std`, `min`, `max`, quartiles) for numerical columns.
- Calculate the correlation matrix between `Cases`, `Recovered`, `Deaths`, and `Tests`.
- Visualize the correlations using a Seaborn heatmap to identify relationships between metrics.

---

# 📈 Visualizing Mortality Rate

- Calculate the `Mortality_Rate` (Deaths / Cases) and `Recovery_Rate` (Recovered / Cases).
- Filter the dataset to include only countries with more than 10,000 cases for a reliable rate.
- Identify and visualize the top 5 countries with the highest mortality rates using a bar plot.

---

# 🌍 Regional Analysis

- Group the data by `continent` and sum the `Cases` and `Deaths`.
- Melt the DataFrame to prepare it for a grouped bar chart.
- Create a visualization comparing total cases and deaths across different continents, using a logarithmic scale for clarity.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| 🐍 Python | Core Programming Language |
| 🐼 Pandas | Data Manipulation & Analysis |
| 🔢 NumPy | Numerical Operations |
| 📉 Matplotlib | Base Plotting Library |
| 📊 Seaborn | Advanced Statistical Visualization |

---

# 📈 Results & Insights

- ✅ Successfully cleaned and prepared a global COVID-19 dataset.
- ✅ Identified the countries with the highest absolute number of cases.
- ✅ Discovered strong correlations between testing, cases, and recoveries.
- ✅ Highlighted countries with severe mortality rates among significantly affected populations.
- ✅ Provided a clear comparative view of the pandemic's impact across continents.

---

# 🏆 Advantages

| Advantage | Description |
|----------|-------------|
| 🧹 Clean Pipeline | Robust data cleaning handles common dataset issues |
| 📉 Insightful | Focuses on derived metrics (rates) rather than just raw counts |
| 🖼️ Visual | Clear and informative charts using Seaborn |
| 🛡️ Reliable | Filters out low-case countries for more accurate mortality analysis |

---

# 👤 Author

<div align="center">

# Tirth Donga

🎓 Python COVID-19 Data Analysis Project

---

### ⭐ Thank You For Visiting This Project ⭐

Made with ❤️ using Python, Pandas & Seaborn

</div>
