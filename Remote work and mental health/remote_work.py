import pandas as pd
df = pd.read_csv("C:/Users/ADMIN/Documents/My projects/MindScape-Exploring-Mental-Health-Trends/Remote work and mental health/Impact_of_Remote_Work_on_Mental_Health.csv")

#Inspect the data 
df.head()
df.info()
df.describe()

#Handling missing values 
df.isnull().sum()
df.dropna()

#Checking for duplicates
df.duplicated().sum()

# Save the cleaned dataset to a CSV file
df.to_csv(r'C:/Users/ADMIN/Documents/My projects/remote_work_cleaned.csv', index=False)

print("Cleaned dataset saved successfully!")

