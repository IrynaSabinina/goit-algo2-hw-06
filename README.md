# goit-algo2-hw-06

This repository contains solutions for two tasks related to data processing and big data analysis.

## Task 1: **Password Uniqueness Check using Bloom Filter**

### Overview
The task involves implementing a **Bloom Filter** to check whether a password has been used before. The Bloom Filter is a probabilistic data structure that allows for efficient membership testing with the possibility of false positives but no false negatives. This task demonstrates the concept of using space-efficient data structures for large-scale data processing.

### Features:
- **Bloom Filter Implementation**: A custom implementation of the Bloom Filter to handle large datasets efficiently.
- **Password Uniqueness Check**: A function that checks if a password has been used previously without storing the actual passwords.
  
### Files:
- `task1.py`: Main script to demonstrate the Bloom Filter functionality.


### Installation Instructions:
1. Make sure you have **Python** installed on your system.
2. Clone or download the repository to your local machine.
3. Navigate to the folder where the files are located.

```bash
# Install the necessary package
pip install mmh3
```
### Usage:

The main script to run is task1.py. It contains the implementation of the Bloom Filter.

You can test the Bloom Filter with the example code provided inside task1.py.

```bash
python3 task1.py
```

**Expected Output:**
```bash
Пароль 'password123' — вже використаний.
Пароль 'newpassword' — унікальний.
Пароль 'admin123' — вже використаний.
Пароль 'guest' — унікальний.
```

## Task 2: Comparison of Exact Counting and HyperLogLog
Overview

This task compares two approaches for counting unique IP addresses from a log file:

Exact Counting: Using a set to store unique IP addresses.

HyperLogLog: A probabilistic algorithm to estimate the cardinality of a dataset with a fixed error rate.

### The task includes:

Loading data from a log file.

Implementing both exact counting and HyperLogLog for unique IP address counting.

Comparing the performance (in terms of time and accuracy) of both methods.

### Files:

task2.py: Main script to load data from a log file, perform the unique IP counting, and compare the methods.

hyperloglog.py: Contains the implementation of the HyperLogLog algorithm.

lms-stage-access.log: A sample log file containing IP addresses.

### Installation Instructions:

Ensure you have Python 3 installed on your machine.

Clone or download the repository.

Install the required libraries.

# Install necessary dependencies
```bash
pip install mmh3
```

**Usage:**

The log file lms-stage-access.log must be present in the same directory.

The main script is **task2.py**, which performs the comparison between exact counting and HyperLogLog.

```bash
python3 task2.py
```

**Expected Output:**
```bash
Завантаження даних з файлу...
Підрахунок точним методом...
Підрахунок за допомогою HyperLogLog...

Результати порівняння:
Метод               Унікальні елементи      Час виконання (сек.)
Точний підрахунок   3                       0.001234
HyperLogLog         3                       0.000123
Час завантаження файлу: 0.002345 сек.
```
