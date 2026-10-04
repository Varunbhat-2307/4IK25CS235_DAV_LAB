from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(Path(__file__).with_name("student_data.csv"), sep=";")
print("Dataset Shape : ",df.shape)
print(df.head())
print("Dataset Information : ")
df.info()
print("Dataset Description : \n",df.describe())
plt.figure(figsize=(6,4))
sns.histplot(df["G3"], bins=20,kde=True,color="steelblue")
plt.title("Distribution of Final Grade")
plt.xlabel("Final Grade")
plt.ylabel("Frequency")
plt.show()
plt.figure(figsize=(6,4))
sns.boxplot(x="studytime",y="G3",data=df,color="steelblue")
plt.title("Final Grade across Study Time Levels")
plt.xlabel("Study Time (1=Low 4=High)")
plt.ylabel("Final Grade")
plt.show()
plt.figure(figsize=(6,4))
sns.scatterplot(x="G1",y="G3",hue="sex",data=df,palette="coolwarm")
plt.title("First Period Grade vs Final Grade")
plt.xlabel("G1 (First Period Grade)")
plt.ylabel("G3 (Final Grade)")
plt.show()
sns.pairplot(df[["age","studytime","G1","G2","G3","sex"]],hue="sex")
plt.suptitle("Pair Relations",y=1.02)
plt.show()
numeric_cols = ["age","studytime","failures","absences","G1","G2","G3"]
plt.figure(figsize=(8,6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()