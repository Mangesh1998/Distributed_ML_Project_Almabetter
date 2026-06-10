# Distributed Machine Learning & Hadoop MapReduce Project

This repository contains a comprehensive big data analytics and machine learning workflow. The project leverages **PySpark** for parallelized data processing and machine learning modeling, along with **Hadoop MapReduce** for distributed data transformation and analysis.

---

## 📂 Repository Structure

```directory
├── Distributed_ML.ipynb                          # Jupyter notebook with PySpark workflows
├── bank.csv                                       # Banking marketing campaign dataset
├── Data Analysis and Management using Hadoop...   # PDF project documentation / report
├── .gitignore                                     # Standard Git ignore rules for Python & Jupyter
├── README.md                                      # Project documentation (this file)
└── Hadoop MapReduce Code-20240824T194051Z-001/    # Directory containing MapReduce scripts
    ├── Data transformation MapReduce codes/
    │   ├── Question 1/                            # Avg balance per job type
    │   │   ├── mapper1.py
    │   │   └── reducer1.py
    │   ├── Question 2/                            # Housing loan counts by education level
    │   │   ├── mapper 2.py
    │   │   └── reducer 2.py
    │   └── Question 3/                            # Subscription status count by month
    │       ├── mapper 3.py
    │       └── reducer 3.py
    └── data analysis MapReduce codes/
        ├── Question 1/                            # Contact duration per previous outcome (poutcome)
        │   ├── mapper 4.py
        │   └── reducer 4.py
        └── Question 2/                            # Average balance per age group
            ├── mapper.py
            └── reducer.py
```

---

## 📊 Dataset: Bank Marketing Campaigns (`bank.csv`)

The project uses the classic bank marketing dataset, which describes direct marketing campaigns (phone calls) of a Portuguese banking institution. The goal is to predict whether a client will subscribe to a term deposit (column `y` / `label`).

### Key Fields:
*   **Demographics**: `age`, `job`, `marital`, `education`, `default`, `balance`
*   **Campaign Details**: `housing`, `loan`, `contact`, `day`, `month`, `duration`, `campaign`, `pdays`, `previous`, `poutcome`
*   **Target**: `y` (binary: `yes` / `no`)

---

## ⚡ Task 1: PySpark Data Parallelism & Machine Learning

The primary notebook `Distributed_ML.ipynb` contains the PySpark workflow structured as follows:

### 1. Data Preparation & Repartitioning
*   **Initialization**: Configures a robust `SparkSession` with custom executor/driver memory parameters and shuffle partitions.
*   **Data Parallelism**: The dataset is partitioned into 4 distinct segments using the `balance` column, ensuring optimal partition distribution for downstream operations.

### 2. Parallel Data Aggregations
*   **Average Account Balance by Job**: Computes the average account balance grouped by the employee's job category.
*   **Top 5 Age Groups with Highest Loans**: Sorts and retrieves the age brackets with the highest total financial balances (loans).

### 3. Distributed Model Training
*   **Algorithm**: Random Forest Classifier.
*   **Pipeline**: Automates features scaling and indexing using `StringIndexer` for categorical fields and `VectorAssembler` to group features into a unified vector.
*   **Results**: Achieved a test Area Under the ROC Curve (**AUC**) of **~0.875**.
*   **Model Persistence**: The trained ML pipeline is saved to `/ml_model_trained` for easy loading.

### 4. Resource Monitoring & Task Management
*   **Event Logging**: Enabled Spark event logging to capture JVM resource metrics and performance.
*   **Parallel Preprocessing**: Tasks are modularized into independent functions to run concurrently during preprocessing stage optimization.

---

## 🛠️ Task 2: Hadoop MapReduce Scripts

A set of standard MapReduce mapper/reducer Python scripts are provided under `Hadoop MapReduce Code-...` to process `bank.csv` using Hadoop Streaming.

### Data Transformation Workflows
1.  **Question 1**: Calculates the average account balance per job type.
2.  **Question 2**: Aggregates housing loan status counts (`yes`/`no`) across different education levels.
3.  **Question 3**: Compiles subscription counts (successes/failures) segmented by calendar month.

### Data Analysis Workflows
1.  **Question 1**: Measures the average call contact duration (in seconds) corresponding to each previous campaign outcome (`poutcome`).
2.  **Question 2**: Computes the average account balance per individual age group.

---

## 🚀 How to Execute the Project

### Running PySpark Notebook
Ensure you have PySpark installed:
```bash
pip install pyspark
```
Run `Distributed_ML.ipynb` locally or upload it to Google Colab. Make sure to update the path to `bank.csv` as per your environment.

### Running MapReduce Scripts (Hadoop Streaming)
To run these Python MapReduce scripts locally for testing, you can simulate Hadoop streaming via terminal pipes:

```bash
# Example: Running Data Analysis Question 2 (Average balance per age)
cat bank.csv | python "Hadoop MapReduce Code-20240824T194051Z-001/data analysis MapReduce codes/Question 2/mapper.py" | sort | python "Hadoop MapReduce Code-20240824T194051Z-001/data analysis MapReduce codes/Question 2/reducer.py"
```

To run on a live Hadoop Cluster:
```bash
hadoop jar /path/to/hadoop-streaming.jar \
  -input /user/hadoop/bank.csv \
  -output /user/hadoop/output \
  -mapper "python mapper.py" \
  -reducer "python reducer.py" \
  -file mapper.py \
  -file reducer.py
```

---

