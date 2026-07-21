<div align="center">

# 😃 World Happiness Report Analysis
### *Exploring Global Happiness Scores and Contributing Factors (2015)*

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Library-Seaborn-4C72B0?style=for-the-badge)
![Data Visualization](https://img.shields.io/badge/Concept-Data_Visualization-orange?style=for-the-badge)

</div>

---

# 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📁 Data Loading & Inspection](#-data-loading--inspection)
- [🧹 Data Cleaning & Renaming](#️-data-cleaning--renaming)
- [📊 Visualizing Extremes](#-visualizing-extremes)
- [📉 Correlation Analysis](#-correlation-analysis)
- [📈 Regression Analysis](#-regression-analysis)
- [🌍 Regional Happiness](#-regional-happiness)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [👤 Author](#-author)

---

# 📌 Overview

**World Happiness Report Analysis** is a data exploration project that investigates the 2015 World Happiness Report dataset. Utilizing **Pandas**, **Matplotlib**, and **Seaborn**, the project uncovers the happiest and least happy countries, analyzes the correlations between happiness scores and economic/social factors, and visualizes regional trends.

---

# 🎯 Problem Statement

The objective is to analyze global happiness data to determine which factors (such as GDP, life expectancy, family support, etc.) most strongly correlate with a country's happiness score. By renaming columns for clarity and generating intuitive visualizations, the project aims to present clear insights into global well-being.

---

# ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📁 Data Ingestion | Loading the 2015 World Happiness Report CSV |
| 🧹 Data Cleaning | Renaming lengthy columns and checking for missing values |
| 📊 Extreme Analysis | Visualizing the top 5 happiest vs. bottom 5 least happy countries |
| 📉 Correlation Heatmap | Identifying relationships between happiness and contributing factors |
| 📈 Regression Plots | Detailed look at how GDP and Life Expectancy affect Happiness |
| 🌍 Regional Grouping | Averaging and visualizing happiness scores by geographic region |

---

# 🏗️ Project Structure

```text
📦 Project2_happyness/
│── 📄 2015.csv
│── 📄 happiness_analysis.ipynb
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
  ├── Rename Columns & Check for NaNs
  ├── Visualize Top 5 & Bottom 5 Countries
  ├── Calculate Descriptive Stats
  ├── Generate Correlation Heatmap
  ├── Create Regression Plots (GDP & Life Expectancy)
  └── Regional Average Score Visualization
```

---

# 📁 Data Loading & Inspection

- Load the `2015.csv` dataset.
- View the initial rows and column schema to understand the available metrics (e.g., Happiness Score, GDP per Capita, Health).

---

# 🧹 Data Cleaning & Renaming

- Rename long column names for easier access (e.g., `'Economy (GDP per Capita)'` to `'GDP_per_Capita'`).
- Drop any potential duplicate rows.
- Verify data integrity by checking for missing values (resulting in 0 missing values).

---

# 📊 Visualizing Extremes

- Extract the top 5 (head) and bottom 5 (tail) countries based on their Happiness Score.
- Concatenate them into a single DataFrame.
- Create a Seaborn bar plot using a custom color palette to starkly contrast the happiest (green) and least happy (red) nations.

---

# 📉 Correlation Analysis

- Select key numerical columns determining happiness.
- Calculate summary statistics (`describe()`).
- Generate a correlation matrix and visualize it using a Seaborn heatmap to see which factors (like GDP or Family) have the strongest positive correlation with the Happiness Score.

---

# 📈 Regression Analysis

- Create side-by-side regression plots (`sns.regplot`).
- **Plot 1:** Happiness Score vs. GDP per Capita.
- **Plot 2:** Happiness Score vs. Life Expectancy.
- These plots highlight the positive linear trends between economic/health factors and overall happiness.

---

# 🌍 Regional Happiness

- Group the dataset by `Region` and calculate the mean `Score`.
- Sort the regions from highest average happiness to lowest.
- Generate a bar plot showing the average happiness score per geographic region, identifying which parts of the world are generally happier.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| 🐍 Python | Core Programming Language |
| 🐼 Pandas | Data Manipulation & Analysis |
| 🔢 NumPy | Numerical Operations |
| 📉 Matplotlib | Base Plotting Library |
| 📊 Seaborn | Statistical Data Visualization |

---

# 📈 Results & Insights

- ✅ Demonstrated clear disparities between the top and bottom countries in global happiness.
- ✅ Confirmed strong positive correlations between Happiness Score, GDP per Capita, and Life Expectancy.
- ✅ Visualized regional trends, showing Western Europe and North America leading in average happiness.
- ✅ Cleaned and structured the dataset for easy programmatic access.

---

# 🏆 Advantages

| Advantage | Description |
|----------|-------------|
| 🧹 Clean Data | Renamed columns make code readable and maintainable |
| 🖼️ Intuitive Visuals | Uses custom palettes and side-by-side plots for easy comparison |
| 📉 Statistical Focus | Highlights trends using regression lines and correlation matrices |
| 🌍 Global Context | Aggregates data regionally for macro-level insights |

---

# 👤 Author

<div align="center">

# Tirth Donga

🎓 Python World Happiness Data Analysis Project

---

### ⭐ Thank You For Visiting This Project ⭐

Made with ❤️ using Python, Pandas & Seaborn

</div>
