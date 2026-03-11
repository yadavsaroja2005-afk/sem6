# compact_dataprocessing.py
import pandas as pd
import numpy as np

# --- File paths (absolute) ---
csv_path = "D:/practice/dataframe/employee.csv"
json_path = "D:/practice/dataframe/employee.json"
processed_path = "D:/practice/dataframe/employee_processed.csv"

# --- Read CSV and JSON ---
df_csv = pd.read_csv(csv_path)
df_json = pd.read_json(json_path)

# --- Handle missing values ---
df_csv['Age'].fillna(df_csv['Age'].mean(), inplace=True)
df_csv['Salary'].fillna(df_csv['Salary'].mean(), inplace=True)

# --- Handle outliers (IQR) ---
for col in ['Age', 'Salary']:
    Q1, Q3 = df_csv[col].quantile([0.25, 0.75])
    IQR = Q3 - Q1
    df_csv[col] = np.clip(df_csv[col], Q1 - 1.5*IQR, Q3 + 1.5*IQR)

# --- Filtering, Sorting, Grouping, Transformation ---
high_salary = df_csv[df_csv['Salary'] > 45000]
sorted_df = df_csv.sort_values('Salary', ascending=False)
avg_salary_dept = df_csv.groupby('Department')['Salary'].mean()
df_csv['Salary_in_K'] = df_csv['Salary'] / 1000

# --- Print outputs ---
print("Filtered (Salary>45000):\n", high_salary)
print("\nSorted by Salary:\n", sorted_df)
print("\nAverage Salary by Department:\n", avg_salary_dept)
print("\nTransformed CSV:\n", df_csv)

# --- Save processed CSV ---
df_csv.to_csv(processed_path, index=False)
print(f"\nProcessed CSV saved at: {processed_path}")
