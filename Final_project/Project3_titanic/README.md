<div align="center">

# 🚢 Titanic Survival Analysis
### *Machine Learning Preprocessing & Exploratory Data Analysis*

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Library-Seaborn-4C72B0?style=for-the-badge)
![EDA](https://img.shields.io/badge/Concept-EDA-orange?style=for-the-badge)

</div>

---

# 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📁 Data Loading & Label Creation](#-data-loading--label-creation)
- [🧹 Data Cleaning & Imputation](#️-data-cleaning--imputation)
- [📊 Survival by Gender](#-survival-by-gender)
- [📉 Survival by Passenger Class](#-survival-by-passenger-class)
- [📈 Age Distribution & Survival](#-age-distribution--survival)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [👤 Author](#-author)

---

# 📌 Overview

**Titanic Survival Analysis** is an Exploratory Data Analysis (EDA) project focused on the famous Titanic dataset (specifically using `test.csv`). The project demonstrates crucial data preprocessing steps, including missing value imputation and feature engineering, followed by insightful visualizations using **Seaborn** to understand survival patterns based on demographics like gender, passenger class, and age.

---

# 🎯 Problem Statement

The objective is to take raw, incomplete passenger data and prepare it for analysis. By handling missing values (Age, Fare, Embarked) and dropping highly sparse columns (Cabin), we create a clean dataset. We then explore how survival rates (using a simplified heuristic for demonstration) correlate with passenger gender, class, and age groups.

---

# ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📁 Data Ingestion | Loading Titanic test data and generating a mock 'Survived' label |
| 🧹 Data Imputation | Filling missing numerical values with medians and categorical with mode |
| 🗑️ Feature Selection | Dropping columns with excessive missing data (e.g., Cabin) |
| 📊 Gender Analysis | Visualizing survival counts grouped by passenger sex |
| 📉 Class Analysis | Exploring the relationship between ticket class (Pclass) and survival |
| 📈 Age Grouping | Binning ages into categories (Child, Teen, Adult, Senior) for detailed analysis |

---

# 🏗️ Project Structure

```text
📦 Project3_titanic/
│── 📄 test.csv
│── 📄 titanic_eda.ipynb
└── 📄 README.md
```

---

# 🔄 Project Workflow

```text
Start
  │
  ▼
Load Data & Create Mock Labels
  │
  ├── Data Cleaning (Impute NaNs, Drop Cabin)
  ├── Inspect Cleaned Data Stats
  ├── Visualize Survival by Gender
  ├── Visualize Survival by Pclass
  └── Create Age Bins & Visualize Survival by Age Group
```

---

# 📁 Data Loading & Label Creation

- Load `test.csv` using Pandas.
- Since `test.csv` lacks the target variable, a mock `Survived` column is created using a simple heuristic (`1 if female else 0`) for demonstration purposes in the visualizations.
- Initial inspection reveals missing values in `Age`, `Fare`, and `Cabin`.

---

# 🧹 Data Cleaning & Imputation

- **Age & Fare:** Missing values are imputed using the column `median` to avoid outlier skew.
- **Embarked:** Missing values are filled with the `mode` (most frequent port).
- **Cabin:** Dropped entirely due to a high percentage of missing values.
- Post-cleaning validation confirms 0 missing values across all columns.

---

# 📊 Survival by Gender

- Generates a Seaborn `countplot` to visualize the survival distribution separated by `Sex`.
- Demonstrates the stark contrast in survival rates (based on the applied heuristic/historical context) between males and females.

---

# 📉 Survival by Passenger Class

- Creates a `countplot` exploring survival outcomes across the three passenger classes (`Pclass` 1, 2, and 3).
- Highlights how socio-economic status impacted survival chances on the Titanic.

---

# 📈 Age Distribution & Survival

- **Overall Distribution:** Uses a `histplot` to show the general age distribution of passengers.
- **Feature Engineering:** Uses `pd.cut` to categorize continuous `Age` data into discrete bins: 'Child', 'Teen', 'Adult', and 'Senior'.
- **Age Group Survival:** Visualizes survival counts within these newly created age bins, providing a clearer picture of demographic survival patterns.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| 🐍 Python | Core Programming Language |
| 🐼 Pandas | Data Preprocessing, Imputation & Binning |
| 🔢 NumPy | Numerical Operations |
| 📉 Matplotlib | Figure Layout & Plotting |
| 📊 Seaborn | Advanced Categorical Visualizations |

---

# 📈 Results & Insights

- ✅ Successfully cleaned a messy dataset by applying appropriate imputation techniques.
- ✅ Engineered new features (Age Groups) to facilitate better categorical analysis.
- ✅ Visualized key historical trends, such as the "women and children first" protocol and class disparities.

---

# 🏆 Advantages

| Advantage | Description |
|----------|-------------|
| 🧹 Clean Handling | Robust strategies for dealing with missing data (median/mode imputation) |
| 🛠️ Feature Eng. | Converts continuous variables into meaningful categories for clearer analysis |
| 🖼️ Clear Visuals | Uses Seaborn's color palettes and grid layouts for professional plots |
| 🎓 Foundational | Excellent template for standard Machine Learning data preprocessing |

---

# 👤 Author

<div align="center">

# Tirth Donga

🎓 Python Titanic EDA Project

---

### ⭐ Thank You For Visiting This Project ⭐

Made with ❤️ using Python, Pandas & Seaborn

</div>
