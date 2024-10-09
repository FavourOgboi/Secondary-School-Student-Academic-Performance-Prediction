# Student-Academic-Performance-Prediction

![Example Image](/images/student.jpeg)
### TEAM DATAVERSE
***
This project analyzes student academic performance based on various factors such as foundational knowledge, study hours, and family background. The goal is to predict students' academic success and improve educational outcomes by providing valuable insights to educators.

# Project Overview

## 2. Dataset Description

The dataset used for this project was collected from various educational institutions in Ikorodu, comprising both public and private schools. Specifically, I visited the following schools:

1. **Private College - KingsField**
2. **Public School - Elepe**
3. **Private School - Tiakod College**

During my visits, I interviewed **100 students** who were provided with a questionnaire to fill out. While some schools did not permit data collection, these three institutions facilitated the process by allowing me to gather valuable insights.

## Folder Arrangement

The project folder is organized as follows:

```
MLmodel
  ├── .ipynb_checkpoints 
  ├── model.ipynb 
  ├── test_inputs.parquet 
  ├── test_targets.parquet 
  ├── train_inputs.parquet 
  ├── train_targets.parquet 
  ├── val_inputs.parquet 
  └── val_targets.parquet

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

## Database Structuring

For this project, I utilized an SQLite database to store the collected data. The database schema was structured to efficiently manage student information and survey responses. I employed **SQLAlchemy** to facilitate the querying of the database, allowing for seamless interaction with the data.

## Data Pipeline

I built a data pipeline using Python, which was crucial for processing the collected data. This pipeline is located within the GitHub repository and consists of various scripts designed to handle data insertion and transformation tasks.

## Data Warehousing

A data warehousing solution was also created using Python, which helped in organizing and managing the data effectively. This warehouse allows for easy access and retrieval of information for analysis.

## Prediction Model

I developed a prediction model that analyzes the survey data to provide insights into student performance and behavior. This model was trained on the dataset collected and utilized various machine learning techniques to ensure accuracy.

## Web Application Deployment

To present the insights and predictions from the model, I deployed a web application using **Streamlit**. Users can access this application to view insights and make predictions based on the data collected. To assess the app, you can visit the following link: [DataVerse Web Application](https://magical-starburst-aa756b.netlify.app).

