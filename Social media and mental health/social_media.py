import pandas as pd
df = pd.read_csv("C:/Users/ADMIN/Documents/My projects/MindScape-Exploring-Mental-Health-Trends/Social media and mental health/smmh.csv")

#Inspect the data 
df.head()
df.info()
df.describe()

#Handling missing values 
df.isnull().sum()
df.dropna()

#Checking for duplicates
df.duplicated().sum()

df.columns()
# Rename the columns
df = df.rename(columns={
    '1. What is your age?': 'Age',
    '2. Gender': 'Gender',
    '3. Relationship Status': 'Relationship_Status',
    '4. Occupation Status': 'Occupation_Status',
    '5. What type of organizations are you affiliated with?': 'Organization_Type',
    '6. Do you use social media?': 'Use_Social_Media',
    '7. What social media platforms do you commonly use?': 'Common_Platforms',
    '8. What is the average time you spend on social media every day?': 'Avg_Time_Social_Media',
    '9. How often do you find yourself using Social media without a specific purpose?': 'Use_Without_Purpose',
    '10. How often do you get distracted by Social media when you are busy doing something?': 'Distracted_By_Social_Media',
    '11. Do you feel restless if you haven\'t used Social media in a while?': 'Restless_Without_Social_Media',
    '12. On a scale of 1 to 5, how easily distracted are you?': 'Distraction_Level',
    '13. On a scale of 1 to 5, how much are you bothered by worries?': 'Bothered_By_Worries',
    '14. Do you find it difficult to concentrate on things?': 'Difficulty_Concentrating',
    '15. On a scale of 1-5, how often do you compare yourself to other successful people through the use of social media?': 'Compare_On_Social_Media',
    '16. Following the previous question, how do you feel about these comparisons, generally speaking?': 'Feelings_About_Comparison',
    '17. How often do you look to seek validation from features of social media?': 'Seek_Validation_Social_Media',
    '18. How often do you feel depressed or down?': 'Feel_Down',
    '19. On a scale of 1 to 5, how frequently does your interest in daily activities fluctuate?': 'Fluctuating_Interest_Daily_Activities',
    '20. On a scale of 1 to 5, how often do you face issues regarding sleep?': 'Sleep_Issues'
})

# Check the new column names
print(df.columns)

# Save the cleaned dataset to a CSV file
df.to_csv(r'C:/Users/ADMIN/Documents/My projects/social_media_cleaned.csv', index=False)

print("Cleaned dataset saved successfully!")