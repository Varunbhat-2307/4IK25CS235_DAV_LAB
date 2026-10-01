from pathlib import Path

import pandas as pd

data_path = Path(__file__).with_name("student_performance_dataset.csv")
df = pd.read_csv(data_path)
print("First 5 rows of the dataset")
print(df.head())
print("\nStatistical Summary:")
print(df.describe())
numeric_cols = ["Study_Hours_per_Week","Attendance_Rate","Past_Exam_Scores","Final_Exam_Score"]
df.loc[0,"Study_Hours_per_Week"] =  120
df.loc[1,"Attendance_Rate"] = 250
df.loc[2,"Past_Exam_Scores"] = -20
df.loc[3,"Final_Exam_Score"] = 200
print("\nInserted a few artificial outlier values for demonstratrion")
print("\n----IQR Method----\n")
for col in numeric_cols:
  Q1 = df[col].quantile(0.25)
  Q3 = df[col].quantile(0.75)
  IQR = Q3 - Q1
  lower = Q1 - 1.5*IQR
  upper = Q3 + 1.5*IQR
  outliers = df[(df[col]<lower) | (df[col]>upper)]
  print(f"{col}: {len(outliers)} outlier(s) found (limits : {lower:.2f} to {upper:.2f})")
print("\n------ Z-Score Method ------\n")
for col in numeric_cols:
  z_scores = (df[col] - df[col].mean()) / df[col].std()
  outliers = df[z_scores.abs() > 3]
  print(f"{col}: {len(outliers)} outlier(s) found (|z| > 3)")
df_treated = df.copy()
print("\n ------- Treating Outliers (Capping using IQR limits) ------")
for col in numeric_cols:
  Q1 = df[col].quantile(0.25)
  Q3 = df[col].quantile(0.75)
  IQR = Q3 - Q1
  lower = Q1 - 1.5*IQR
  upper = Q3 + 1.5*IQR
  df_treated[col] = df_treated[col].clip(lower,upper)
  print(f"{col}: values capped between {lower:.2f} and {upper:.2f}")
print("\nStatistics BEFORE treatment:")
print(df[numeric_cols].describe())
print("\nStatistics AFTER treatment:")
print(df_treated[numeric_cols].describe())
output_path = Path(__file__).with_name("student_performance_dataset_treated.csv")
df_treated.to_csv(output_path, index=False)
print(f"\nTreated dataset saved as '{output_path.name}'")
print("Program Executed Successfully.")