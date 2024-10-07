from sqlalchemy import create_engine, text
import pandas as pd

db_path = 'student_database.db'

engine = create_engine(f'sqlite:///{db_path}')
# function for inserting data into the SQLite database
def insert_data(db_engine, table_name, data):
    
    with db_engine.connect() as conn:
        
        placeholders = ', '.join(['?'] * len(data.columns))
        
        sql = f'INSERT INTO {table_name} VALUES ({placeholders})'
        
        conn.execute(text(sql), tuple(data.values.flatten()))

# Loading new data from a CSV file
new_data = pd.read_csv('new_data.csv')  # Ensuring the CSV matches database structure

for index, row in new_data.iterrows():
    
    insert_data(engine, 'student_performance', row)  # Inserting data into the specified table

print("New data has been added to the database.")  # Indicating completion of data insertion
