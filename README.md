# Student-Academic-Performance-Analysis-And-Insights

![Example Image](/images/student.jpeg)
***
### TEAM DATAVERSE

This project analyzes student the African student academic performance based on various factors such as foundational knowledge, study hours, and family background. The goal is to analyse students' academic success and improve educational outcomes by providing valuable insights to educators.

**NB**: NO DATA WAS GENERATED USING AI TO AVOID SKEWNESS

**TEAM MEMBERS AND ROLES**
- GIFT ZARA > DATA ANALYST
- VINCENT FAVOUR > DATA ANALYST

# Project Overview
***
## 2. Dataset Description

The dataset used for this project was collected from various educational institutions in Ikorodu, comprising both public and private schools. Specifically, we visited the following schools:

1. **Private College - KingsField**
2. **Public School - Elepe**
3. **Private School - Tiakod College**

During my visits, we interviewed **100 students** who were provided with a questionnaire to fill out. While some schools did not permit data collection, these three institutions facilitated the process by allowing us to gather valuable insights.
***
![Form](/images/formimg.jpeg)
***

## 3. TOOLS/SKILLS UTILIZED AND ANALYST
- EXCEL - Data Analyst Zara
- PYTHON - Data Analst Vincent & Data Analyst Zara
- SQLite - Data Analst Vincent
- SQLAlchemy - Data Analyst Vincet
- HTML - Data Analyst Vincet
- CSS - Data Analyst Vincet
- Bootstrap - Data Analyst Vincet
- INLINE JS - Data Analyst Vincet
***
## Folder Arrangement

The project folder is organized as follows:

```
Schema 
  ├── .ipynb_checkpoints 
  ├── create_db.ipynb 
  ├── data_insertion_pipeline.py 
  ├── db-test.ipynb 
  |── student_database.db 
  └── warehouse_schema_creation.py

app 
  ├── DataVerse-CSS │ 
      ├── insight.css │ 
      ├── our_team.css  
      │ 
      └── style.css 
  ├── DataVerse-HTML 
    ├── other_insight 
        │ 
        ├── insight.html 
        |__ insight2.html To insight6.html Files
  │ 
  ├── our_team.html 
  
  ├── data │ 
    ├── .ipynb_checkpoints 
    │ 
    ├── Survey_Form 
    │  
    │ ├── QUESTIONAIRE.docx 
    │ 
    │ 
    ├── Raw-Student-Survey-Data.xlsx 
    │ 
    │ 
    ├── processed_survey_data.csv 
    │ 
    │ 
    └── processed_survey_data.xlsx 
    ├── docs 
    |____ A Lot of Insight PNG and JPG
    │ 
    └── images 
    |_____ A lot of images
    ├── notebook 
    │ 
    ├── .ipynb_checkpoints 
    │ 
    ├── Exploratory-data-analysis 
    |______ 6 lot of ipynb folders for 6 diffrent insight categories, in each folder there are ipynb files
    │     
    └── Processing-data.ipynb
```
***
# DASHBOARD - ANALYST ZARA
![Example Image](/images/dashboard.jpeg)
***
## Database Structuring

For this project, We utilized an SQLite database to store the collected data. The database schema was structured to efficiently manage student information and survey responses. I employed **SQLAlchemy** to facilitate the querying of the database, allowing for seamless interaction with the data.

```python
  import pandas as pd
from sqlalchemy import create_engine

# paths specifications 
csv_file_path = '../data/processed_survey_data.csv' 
db_path = 'student_database.db' 

# Creating an SQLite database connection
engine = create_engine(f'sqlite:///{db_path}')

# SNIPPET
```
***
## Data Pipeline

I built a data pipeline using Python, which was crucial for processing the collected data. This pipeline is located within the GitHub repository and consists of various scripts designed to handle data insertion and transformation tasks.

``` python
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

# SNIPPER

```
***
## Data Warehousing

A data warehousing solution was also created using Python, which helped in organizing and managing the data effectively. This warehouse allows for easy access and retrieval of information for analysis.
```python

csv_file_path = '../data/processed_survey_data.csv'
db_path = 'student_database.db'

# Creating an SQLite database connection
engine = create_engine(f'sqlite:///{db_path}')

# Loading the processed_survey_data CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Writing the dataFrame to the SQLite database to create my new table)
df.to_sql('student_performance', con=engine, if_exists='replace', index=False)

# SNIPPET

```
***
## Web Application Deployment

To present the insights and predictions from the model, we deployed a web application using **Netlify**. Users can access this application to view insights based on the data collected. To assess the app, you can visit the following link: [DataVerse Web Application](https://magical-starburst-aa756b.netlify.app).
***
