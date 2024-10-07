# importing dependencies
import pandas as pd
from sqlalchemy import create_engine

csv_file_path = '../data/processed_survey_data.csv'
db_path = 'student_database.db'

# Creating an SQLite database connection
engine = create_engine(f'sqlite:///{db_path}')

# Loading the processed_survey_data CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Writing the dataFrame to the SQLite database to create my new table)
df.to_sql('student_performance', con=engine, if_exists='replace', index=False)

print("Database created and data imported successfully.")
