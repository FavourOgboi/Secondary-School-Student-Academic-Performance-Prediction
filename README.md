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

# Some Exploratory Data Analysis (EDA) Questions

### Demographics
- How does gender distribution compare across different classes and departments?
- What are the age group distributions for the student population?
- Are there significant trends in academic performance across different age groups?

### Living Situation
- How does living situation (e.g., with parents, guardians, or alone) influence academic performance?
- Do students living in different conditions (urban vs. rural) exhibit significant performance differences?

### Family Financial Status
- How does family financial status impact students' access to resources (like tutoring and learning materials)?
- Are there performance disparities based on family financial status?

### Parental Involvement
- Do students whose parents attend parent-teacher meetings perform better academically?
- Is there a correlation between parental encouragement for higher education and student motivation to attend university?
- Does the level of parental help with homework correlate with better performance in subjects?

### Extracurricular Activities
- Does participation in extracurricular activities correlate with higher or lower academic performance?
- How does the number of hours spent in extracurricular activities impact students' academic success?

### Attendance and Study Habits
- How does school attendance impact academic performance?
- Is there a correlation between study hours per week and performance in key subjects like Maths, Biology, and English?
- Do students who attend extra tutoring perform better than those who don't?

### Stress, Motivation, and Mental Well-being
- How does stress about schoolwork correlate with student performance?
- Does motivation for attending school influence academic success?
- Do students who have access to counseling services perform better?
- Is there a relationship between confidence in academic ability and actual performance?

### Bullying and Peer Influence
- Do students who experience bullying show poorer academic performance?
- How does peer pressure affect performance in different subjects?

### Academic Performance Across Subjects
- Which subject do students perform best in, and which subject poses the most challenges?
- Are there correlations between performances in different subjects (e.g., does performance in English correlate with performance in Literature)?
- Are there specific classes where students tend to perform better or worse across different subjects?

### Planned Future Endeavors
- How does last exam performance correlate with planned future academic endeavors (e.g., planning to attend university)?
- Is there a relationship between a student's JAMB goal score and their current academic performance?

### Psychological and Social Factors
- How do students who express a desire to drop out perform compared to others?
- Does participation in extracurricular activities or peer relationships influence the decision to consider dropping out?

### Language and Cultural Background
- Is there a difference in academic performance based on the primary language spoken at home?
- Do students who are involved in work outside of school perform differently from those who aren't?

- 
***
### SOME VISUALS 

<table>
  <tr>
    <td><img src="/docs/performdist.png" alt="Image 1" width="200"/></td>
    <td><img src="/docs/department_distribution_bar_chart.png" alt="Image 2" width="200"/></td>
  </tr>
  <tr>
    <td><img src="/docs/avgconf.png" alt="Image 3" width="200"/></td>
    <td><img src="/docs/go.PNG" alt="Image 4" width="200"/></td>
  </tr>
</table>

### SOME INSIGHT GOTTEN

**IMPACT ON GENDER:**
Students who experience bullying frequently tend to have lower performance scores compared to those who have never been bullied. This suggests that experiencing bullying can have a detrimental effect on academic performance, as reflected by a higher proportion of students scoring in lower performance brackets among those frequently bullied.

**BULLYING DEMOGRAPHICS:**
Female students who are frequently bullied are more likely to come from families that struggle to meet basic needs compared to other financial statuses. Conversely, male students show a tendency to experience bullying less frequently than females across all financial statuses, especially those who are financially comfortable.
Both genders show that those who experience bullying less frequently tend to have higher counts in the "Never" category, indicating that financial stability might play a role in the prevalence of bullying experiences.

**ACADEMIC PERFORMANCE ACROSS CLASSES:**
As students progress from SS1 to SS3, there is a clear trend of increasing academic performance, particularly evident in the 70% - 100% category. SS2 stands out with the highest proportion of students achieving top scores, while SS3 maintains this trend with only a minimal percentage of students scoring below 40%.

**EXTRACURRICULAR ACTIVITIES AND PERFORMANCE:**

- **Highest Performance with Less than 5 Hours:**
  Students who spent less than 5 hours in extracurricular activities per week achieved the highest average exam score of 3.30. This suggests that limited involvement in extracurricular activities, allowing more focus on academics, may positively impact performance.

- **Moderate Performance with 5 - 10 Hours:**
  Students who spent 5 to 10 hours on extracurricular activities per week had a slightly lower average score of 3.22, indicating a balance between extracurriculars and academics can still support solid academic outcomes.

- **Lowest Performance with More than 10 Hours:**
  Students who participated in extracurricular activities for more than 10 hours per week had the lowest average score of 2.94. This may suggest that excessive involvement in non-academic activities could hinder academic performance, possibly due to time constraints or burnout.

**Conclusion:**
While some level of extracurricular participation appears beneficial, too many hours devoted to extracurriculars might negatively affect academic performance. A balanced approach is key.

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
