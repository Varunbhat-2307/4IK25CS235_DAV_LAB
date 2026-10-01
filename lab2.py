import numpy as np
import pandas as pd

data = {
    "Name":["Rahul", "Prashanth", "Alia", "Arjun", "Sharath","Vijay", "Sneha", "Rohan",
          "Ananya", "Karan","Meera", "Adish", "Pooja", "Priya", "Kavya","Naman",
          "Nisha", "Nikhil", "Simran", "Tejas","Tanmay", "Sahil", "Diya", "Manish",
          "Riya"],
    "Marks":[84, 93, np.nan,90, 91,67, 85, np.nan, 76, 90,
             86, 78, 89, np.nan, 91,65, 87, 79, 94, np.nan,
             79, 86, 68, 83, 97],
    "Age":  [20, 21, 19, np.nan, 20,23, 21, 19, 22, np.nan,20, 21, 19, 22, 20,
            23, np.nan, 21, 20, 22, np.nan, 23, 21, np.nan, 20],
    "City": ["Mysuru", "Bengaluru", "Hubballi", "Mangaluru", "Belagavi","Mysuru",
             "Dharwad", "Kalaburagi", "Ballari", "Shivamogga",
            "Bengaluru", "Tumakuru", "Mysuru", "Davanagere", "Udupi",
            "Mangaluru", "Hassan", "Vijayapura", "Bidar", "Mysuru",
            "Hubballi", "Hosapete", "Chikkamagaluru", "Raichur", "Bengaluru"]
}
df = pd.DataFrame(data)
print(df)
print("Shape of dataset:",df.shape)
print("Column names:",df.columns.tolist())
print("Data types of each column:",df.dtypes)
print("\nInformation : \n")
df.info()
print("\n\nDiscriptive Statistics (numerical columns):")
print(df.describe())
print("Mean :",df.mean(numeric_only=True))
print("Median :",df.median(numeric_only=True))
print("Mode :",df.mode(numeric_only=True))
print("Standard Deviation:",df.std(numeric_only=True))
print("\nNull Entries : \n")
print(df.isnull())
print("\nTotal Number of Null Entries : \n")
print(df.isnull().sum())
print("\nTotal missing values in dataset :",df.isnull().sum().sum())
print("\nDuplicate rows in dataset:")
print(df[df.duplicated()])
print("Total number of duplicate rows in dataset :",df.duplicated().sum())