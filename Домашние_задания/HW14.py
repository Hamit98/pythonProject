import pandas as pd

file_path = r"C:\Users\User\Desktop\people.csv"
df = pd.read_csv(file_path)

male_df = df[df['Gender'] == 'Male']
male_df.to_csv('male_data.csv', index=False)

older_than_30_df = df[df['Age'] > 30]
older_than_30_df.to_csv('older_than_30_data.csv', index=False)

name_age_df = df[['Name', 'Age']]
name_age_df.to_csv('name_age_data.csv', index=False)

df.to_csv('file_path.csv', index=False)