import numpy as np
import pandas as pd
marks=np.array([80,85,90,95,100])
print("marks:",marks)
print("Mean:",marks.mean())
print(marks.shape)
df = pd.DataFrame({
    "name": [
        "Aarav Sharma", "Isha Verma", "Rohan Mehta", "Priya Nair", "Karan Gupta",
        "Sneha Rao", "Vikram Singh", "Ananya Das", "Manish Kumar", "Pooja Iyer"
    ],
    "marks": [85, np.nan, 76, 88, 67, 95, 81, 73, 90, 78],
    "branch": [
        "Computer Science", "Electronics", "Mechanical", "Information Technology", "Civil",
        "Computer Science", "Electronics", "Mechanical", "Information Technology", "Civil"
    ]
})
print(df)
print(df.describe())
print(df.marks.mean())
print(df.iloc[0:2])
print(df.duplicated())
print(df.isnull().sum())

