# Titanic Dataset Pandas Tips Assignment
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Titanic dataset
# Replace the path if your CSV is in another folder
df = pd.read_csv("Titanic-Dataset.csv")

print("Titanic dataset loaded successfully!\n")

# --------------------------------------------
# Tip 1: View first 5 rows
print("Tip 1: First 5 rows")
print(df.head(), "\n")

# Tip 2: View last 5 rows
print("Tip 2: Last 5 rows")
print(df.tail(), "\n")

# Tip 3: Check dataset shape
print("Tip 3: Shape (rows, columns)")
print(df.shape, "\n")

# Tip 4: Column names
print("Tip 4: Column names")
print(df.columns, "\n")

# Tip 5: Dataset info
print("Tip 5: Dataset info")
print(df.info(), "\n")

# Tip 6: Statistical summary
print("Tip 6: Statistical summary")
print(df.describe(), "\n")

# Tip 7: Select single column
print("Tip 7: Column 'Age'")
print(df["Age"].head(), "\n")

# Tip 8: Select multiple columns
print("Tip 8: Columns 'Name', 'Age', 'Sex'")
print(df[["Name", "Age", "Sex"]].head(), "\n")

# Tip 9: Filter passengers older than 30
print("Tip 9: Passengers older than 30")
print(df[df["Age"] > 30].head(), "\n")

# Tip 10: Filter female passengers
print("Tip 10: Female passengers")
print(df[df["Sex"] == "female"].head(), "\n")

# Tip 11: Count unique values in 'Sex'
print("Tip 11: Count of passengers by gender")
print(df["Sex"].value_counts(), "\n")

# Tip 12: Check missing values
print("Tip 12: Missing values in each column")
print(df.isnull().sum(), "\n")

# Tip 13: Fill missing 'Age' with mean
df["Age"].fillna(df["Age"].mean(), inplace=True)
print("Tip 13: Missing 'Age' after filling")
print(df["Age"].isnull().sum(), "\n")

# Tip 14: Sort dataset by 'Age'
print("Tip 14: Dataset sorted by Age")
print(df.sort_values("Age").head(), "\n")

# Tip 15: Group by gender and calculate average age
print("Tip 15: Average Age by Gender")
print(df.groupby("Sex")["Age"].mean(), "\n")

# Optional: Plot Age distribution
df["Age"].hist()
plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
