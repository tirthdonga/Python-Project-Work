<div align="center">

# 📈 Stock Market Time-Series Analyzer
### *Comparative Financial Data Analysis and Visualization*

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Library-Seaborn-4C72B0?style=for-the-badge)
![Finance](https://img.shields.io/badge/Concept-Financial_Analysis-orange?style=for-the-badge)

</div>

---

# 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📁 Data Loading & Indexing](#-data-loading--indexing)
- [📉 Correlation Analysis](#-correlation-analysis)
- [📈 Trend Visualization](#-trend-visualization)
- [📊 Volume & Returns Analysis](#-volume--returns-analysis)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [👤 Author](#-author)

---

# 📌 Overview

**Stock Market Time-Series Analyzer** is a financial data visualization project that evaluates historical stock prices. By processing daily market data for major tech companies (AAPL, MSFT, NFLX, GOOG), the project explores price correlations, plots comparative closing price trends, visualizes trading volume, and analyzes the distribution of daily returns.

---

# 🎯 Problem Statement

The objective is to ingest raw stock market data, ensure proper chronological ordering, and extract actionable financial insights. The project aims to demonstrate how to visualize the performance of multiple tickers simultaneously, understand the relationship between different price points (Open, High, Low, Close), and calculate daily percentage returns for risk assessment.

---

# ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📁 Data Ingestion | Loading multi-ticker financial data |
| ⏱️ Chronological Sorting | Converting dates and sorting by Ticker and Date |
| 📉 Correlation Heatmap | Analyzing relationships between Open, High, Low, Close, and Volume |
| 📈 Comparative Line Plots | Charting Closing Prices for multiple tech stocks over time |
| 📊 Volume Bar Charts | Visualizing daily trading volume (e.g., for Apple) |
| 🧮 Daily Returns Calc | Computing and plotting the distribution of daily percentage returns |

---

# 🏗️ Project Structure

```text
📦 Project5_stock/
│── 📄 stocks.csv
│── 📄 stock_analysis.ipynb
└── 📄 README.md
```

---

# 🔄 Project Workflow

```text
Start
  │
  ▼
Load Data & Identify Tickers
  │
  ├── Convert Dates & Sort Chronologically
  ├── Generate Financial Metric Correlation Heatmap
  ├── Plot Comparative Closing Prices (Multi-line)
  ├── Isolate AAPL Data for Volume Bar Chart
  └── Calculate & Plot AAPL Daily Returns Distribution
```

---

# 📁 Data Loading & Indexing

- Load the `stocks.csv` file containing daily metrics for multiple companies.
- Identify the unique tickers present in the dataset (AAPL, MSFT, NFLX, GOOG).
- Convert the `Date` column to Pandas datetime objects and sort the DataFrame chronologically by `Ticker` and `Date` to ensure accurate time-series analysis.

---

# 📉 Correlation Analysis

- Select key financial columns (`Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume`).
- Generate a correlation matrix to understand the collinearity of intraday price movements.
- Visualize the matrix using a Seaborn heatmap with a 'Blues' color palette.

---

# 📈 Trend Visualization

- Create a multi-line plot using Seaborn's `lineplot`.
- Map the x-axis to `Date`, y-axis to `Close` price, and use `Ticker` as the `hue` to overlay the performance of Apple, Microsoft, Netflix, and Google on a single chart.

---

# 📊 Volume & Returns Analysis

- **Trading Volume:** Isolate data for a specific ticker (e.g., Apple) and plot a Matplotlib bar chart showing daily trading volume over time.
- **Daily Returns:** Use `.pct_change() * 100` to calculate the daily percentage return for the closing price.
- **Risk Distribution:** Plot a Seaborn `histplot` with Kernel Density Estimation (KDE) to visualize the volatility and distribution of these daily returns.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| 🐍 Python | Core Programming Language |
| 🐼 Pandas | Financial Data Sorting & Percentage Calculations |
| 📉 Matplotlib | Base Plotting (Line & Bar charts) |
| 📊 Seaborn | Advanced Visualization (Heatmaps & KDE overlays) |

---

# 📈 Results & Insights

- ✅ Successfully aligned and sorted multi-ticker financial data chronologically.
- ✅ Provided a clear visual comparison of Big Tech stock performance over the given timeframe.
- ✅ Highlighted trading volume spikes and visualized the frequency of daily gains and losses, aiding in basic risk assessment.

---

# 🏆 Advantages

| Advantage | Description |
|----------|-------------|
| ⏱️ Time-Accurate | Ensures data is sorted chronologically before applying `.pct_change()` |
| 🖼️ Comparative | Multi-line plots allow instant visual comparison of competitors |
| 🧮 Financial Focus | Calculates standard financial metrics like Daily Returns |
| 🧹 Clean Code | Isolates specific tickers (like AAPL) seamlessly for deep dives |

---

# 👤 Author

<div align="center">

# Tirth Donga

🎓 Python Stock Market Analysis Project

---

### ⭐ Thank You For Visiting This Project ⭐

Made with ❤️ using Python, Pandas & Seaborn

</div>
