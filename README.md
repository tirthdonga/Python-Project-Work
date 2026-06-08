# 📊 Data Analyzer and Transformer Program

### *Interactive Python Console Application for Dataset Analysis and Transformation*

---

# 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- 1-[📥 Input Data](#-input-data)
- 2-[📊 Display Data Summary](#-display-data-summary)
- 3-[🧮 Calculate Factorial](#-calculate-factorial)
- 4-[🔍 Filter Data By Threshold](#-filter-data-by-threshold)
- 5-[↕️ Sort Data](#️-sort-data)
- 6-[📈 Dataset Statistics Using UDF](#-dataset-statistics-using-udf)
- 7-[🖨️ Print Current Dataset](#️-print-current-dataset)
- [🚫 Error Handling](#-error-handling)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)

---

# 📌 Overview

The **Data Analyzer and Transformer Program** is a menu-driven Python application that allows users to input, analyze, filter, sort, and transform numerical datasets.

The project demonstrates:

- Functions and User Defined Functions (UDF)
- Recursive Programming
- Variable Length Arguments (*args)
- Keyword Arguments (**kwargs)
- Lambda Functions
- Built-in Functions
- List Operations
- Global Variables
- Match Case Statements
- Error Handling
- Menu Driven Programming

---

# 🎯 Problem Statement

Build a Python console application capable of performing multiple analytical operations on a dataset entered by the user.

The program should:

- Store numerical data
- Generate dataset summaries
- Calculate factorial values
- Filter data using thresholds
- Sort data in different orders
- Compute statistics using custom algorithms
- Handle invalid and empty dataset situations

---

# ✨ Key Features

| Feature | Description |
|----------|------------|
| 📥 Input Data | Store sample or manual dataset |
| 📊 Data Summary | Display min, max, sum and average |
| 🧮 Factorial Calculation | Recursive factorial computation |
| 🔍 Data Filtering | Filter values above threshold |
| ↕️ Data Sorting | Ascending and descending sorting |
| 📈 Dataset Statistics | Statistics using custom logic |
| 🖨️ Print Dataset | Display current stored dataset |
| 📄 Docstring Display | Shows function information |
| ⚠️ Error Handling | Handles empty dataset conditions |
| 🔄 Continuous Menu | Runs until user exits |

---

# 🏗️ Project Structure

```text
📦 Project/
│
├── 📄 data_analyzer.py
│
└── 📄 README.md
```

---

# 🔄 Project Workflow

```text
Program Start
      │
      ▼
 Display Main Menu
      │
      ├── 1 ➜ Input Data
      ├── 2 ➜ Display Data Summary
      ├── 3 ➜ Calculate Factorial
      ├── 4 ➜ Filter Data By Threshold
      ├── 5 ➜ Sort Data
      ├── 6 ➜ Dataset Statistics
      ├── 7 ➜ Print Data
      └── 0 ➜ Exit
```

---

# 📥 Input Data

Allows users to store data in two different ways:

### Options

- Use predefined sample dataset
- Enter custom data manually

### Concepts Used

- Lists
- Loops
- User Input
- Global Variables

### Output

<img src="">

---

# 📊 Display Data Summary

Generates a quick overview of the dataset.

### Information Displayed

- Total Elements
- Minimum Value
- Maximum Value
- Sum Of Values
- Average Value

### Concepts Used

- *args
- **kwargs
- Built-in Functions
- Dynamic Precision Handling

---

# 🧮 Calculate Factorial

Searches the dataset for a user-entered value and calculates its factorial using recursion.

### Concepts Used

- Recursive Functions
- Searching Algorithms
- Conditional Statements

Example:

```text
5! = 120
```

---

# 🔍 Filter Data By Threshold

Filters dataset values according to a threshold entered by the user.

### Concepts Used

- Lambda Functions
- filter()
- Lists

Example:

```text
Threshold = 5

Output:
5, 6, 7, 8, 9, 10
```

---

# ↕️ Sort Data

Sorts the dataset based on user preference.

### Sorting Options

- Ascending Order
- Descending Order

### Concepts Used

- List Sorting
- Match Case
- Boolean Flags

---

# 📈 Dataset Statistics Using UDF

Calculates dataset statistics using custom logic instead of built-in aggregation methods.

### Information Displayed

- Minimum Value
- Maximum Value
- Sum Of Values
- Average Value

### Concepts Used

- User Defined Functions
- Loops
- Manual Calculations

---

# 🖨️ Print Current Dataset

Displays the currently stored dataset.

Example:

```text
Current Data Set:
[3, 4, 1, 5, 8, 9, 6, 2, 7, 10]
```

---

# 🚫 Error Handling

The program contains error handling mechanisms to improve reliability and user experience.

## Features

- Detects empty datasets
- Prevents calculations without data
- Checks for unavailable factorial targets
- Displays user-friendly error messages
- Handles invalid menu selections

### Example Errors

```text
🛑 Error: Dataset is empty.

🛑 Error: Number is not present in dataset.

🛑 You Entered An Invalid Choice.
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core Programming Language |
| 📚 Array | Dataset Storage |
| 🌍 Global Keyword  | Access and modify the dataset globally across multiple functions |
| ⚙️ Functions | Modular Programming |
| 🔄 Recursion | Factorial Calculation |
| 🧩 Lambda | Data Filtering |
| 📄 Docstrings | Function Documentation |
| 🔁 Loops | Iteration |
| 🎛️ Match Case | Menu Handling |
| 🖥️ Console I/O | User Interaction |

---

# 📈 Results & Insights

After executing the program:

- ✅ Dataset can be stored dynamically
- ✅ Summary information is generated instantly
- ✅ Factorials are calculated recursively
- ✅ Data can be filtered efficiently
- ✅ Sorting operations work in both directions
- ✅ Statistics can be calculated without built-in aggregation methods
- ✅ Function documentation is displayed dynamically using docstrings

---

# 🏆 Advantages

| Advantage | Description |
|------------|------------|
| 🎓 Beginner Friendly | Easy to understand and learn |
| 📚 Educational | Covers multiple Python concepts |
| ⚡ Fast Processing | Efficient dataset operations |
| 🧠 Recursion Practice | Demonstrates recursive logic |
| 🔄 Reusable Functions | Modular code structure |
| 🖥️ Lightweight | Runs in any Python terminal |
| 🛠️ Expandable | Easy to add more analysis features |

---

# 👤 Author
<div align="center">

**Tirth Donga**

[![GitHub](https://img.shields.io/badge/GitHub-Tirth_Donga-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tirthdonga)

🎓 Python Programming Project
</div>


---

### ⭐ Thank You For Visiting This Project ⭐

Made with ❤️ using Python
