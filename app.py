import streamlit as st
import joblib
import pandas as pd

# Load the trained model and encoder
model = joblib.load("decision_tree_model.joblib")
encoder = joblib.load("encoder.joblib")
categorical_cols = [
    'Gender', 'Age Group', 'Living Situation', 'Parent Education Level',
    'Family Financial Status', 'Class', 'Department',
    'Performance in English', 'Performance in Maths', 'Performance in Biology',
    'Performance in Physics', 'Performance in Chemistry', 'Performance in Lit in English',
    'Performance in Government', 'Performance in CRS', 'Performance in Commerce',
    'Performance in Accounting', 'Performance in Economics', 'Study Hours per Week',
    'Extra Tutoring', 'School Attendance', 'Experienced Bullying', 'Peer Pressure',
    'Parents Attend Parent-Teacher Meeting', 'Confidence in Academic Ability',
    'Access to Counseling', 'Motivation for Attending School', 'Foundational Knowledge'
]

def predict_input(model, input_data, categorical_cols, encoder):
    input_df = pd.DataFrame([input_data])
    input_encoded = pd.DataFrame(encoder.transform(input_df[categorical_cols]), 
                                 columns=encoder.get_feature_names_out(categorical_cols))
    pred = model.predict(input_encoded)[0]
    return pred

# Streamlit UI
st.set_page_config(page_title="Student Performance Predictor", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")

# Home button
home_button = st.sidebar.button("Go Back to Home")
if home_button:
    st.markdown('<a href="https://magical-starburst-aa756b.netlify.app/" target="_self">Go to Home</a>', unsafe_allow_html=True)

# Our Team button
our_team_button = st.sidebar.button("Back to Our Team")
if our_team_button:
    st.markdown('<a href="https://magical-starburst-aa756b.netlify.app/app/dataverse-html/our_team" target="_self">Go to Our Team</a>', unsafe_allow_html=True)

# Insights button
insights_button = st.sidebar.button("Back to Analysis")
if insights_button:
    st.markdown('<a href="https://magical-starburst-aa756b.netlify.app/app/dataverse-html/insight" target="_self">Go to Insights</a>', unsafe_allow_html=True)

# Main page content
st.title("🎓 Student Performance Predictor")
st.write("### Enter student details to predict performance")

# Form for user input
with st.form("student_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Select your gender", ["Male", "Female"], index=None, placeholder="Choose an option")
        age_group = st.selectbox("Select your age group", ["12 - 14", "15 - 16", "17 - 18"], index=None, placeholder="Choose an option")
        living_situation = st.selectbox("Who do you live with?", ["Both parents", "Single parent", "Guardian"], index=None, placeholder="Choose an option")
        parent_edu = st.selectbox("Highest education level of your parent/guardian", ["No formal education", "Primary school", "Secondary school", "Higher Education", "Post-graduate education"], index=None, placeholder="Choose an option")
        financial_status = st.selectbox("Select your family's financial situation", [
            "We struggle to meet basic needs", "We meet our needs but can't afford luxuries", "We can afford some luxuries", "We are financially comfortable"
        ], index=None, placeholder="Choose an option")
        study_hours = st.selectbox("How many hours do you study per week?", ["Less than 5 hours", "5 - 10 hours", "More than 10 hours", "More than 15 hours"], index=None, placeholder="Choose an option")
        extra_tutoring = st.selectbox("Do you receive extra tutoring?", ["No", "Occasionally", "Regularly"], index=None, placeholder="Choose an option")
        attendance = st.selectbox("How often do you attend school?", ["Occasionally", "Most days", "Every day"], index=None, placeholder="Choose an option")
    
    with col2:
        motivation = st.selectbox("What motivates you to attend school?", [
            "To learn and gain knowledge", "To prepare for a good career", "To meet family expectations", "To avoid being bored at home", "Others"
        ], index=None, placeholder="Choose an option")
        bullying = st.selectbox("Have you experienced bullying?", ["Never", "Occasionally", "Frequently"], index=None, placeholder="Choose an option")
        peer_pressure = st.selectbox("How often do you experience peer pressure?", ["Never", "Occasionally", "Frequently"], index=None, placeholder="Choose an option")
        parent_meeting = st.selectbox("How often do your parents attend parent-teacher meetings?", ["Never", "Sometimes", "Regularly"], index=None, placeholder="Choose an option")
        confidence = st.selectbox("How confident are you in your academic ability?", ["Not confident", "Somewhat confident", "Very confident"], index=None, placeholder="Choose an option")
        counseling = st.selectbox("Do you have access to counseling?", ["Yes", "No", "I'm not sure"], index=None, placeholder="Choose an option")
        foundational_knowledge = st.selectbox("How strong is your foundational knowledge?", ["Weak", "Average", "Strong"], index=None, placeholder="Choose an option")

    department = st.selectbox("Select your department", ["Science", "Arts", "Commerce"], index=None, placeholder="Choose an option")
    class_selection = st.selectbox("Select your class", ['SS1', 'SS2', 'SS3'], index=None, placeholder="Choose your class")
    
    # Based on selected department, set irrelevant subjects to "Nil"
    st.write("### Enter your past academic performance")
    subjects = ["English", "Maths", "Biology", "Physics", "Chemistry", "Lit in English", "Government", "CRS", "Commerce", "Accounting", "Economics"]
    performance = {}
    
    for subject in subjects:
        if department == "Science":
            if subject in ["English", "Maths", "Biology", "Physics", "Chemistry"]:
                performance[subject] = st.selectbox(f"Enter your past performance in {subject}", ["Poor", "Fair", "Good", "Excellent"], index=None, placeholder="Choose an option")
            else:
                performance[subject] = "Nil"
        elif department == "Arts":
            if subject in ["English", "Maths", "Lit in English", "Government", "CRS"]:
                performance[subject] = st.selectbox(f"Enter your past performance in {subject}", ["Poor", "Fair", "Good", "Excellent"], index=None, placeholder="Choose an option")
            else:
                performance[subject] = "Nil"
        elif department == "Commerce":
            if subject in ["English", "Maths", "Commerce", "Accounting", "Economics"]:
                performance[subject] = st.selectbox(f"Enter your past performance in {subject}", ["Poor", "Fair", "Good", "Excellent"], index=None, placeholder="Choose an option")
            else:
                performance[subject] = "Nil"
    
    submitted = st.form_submit_button("Click to Predict Performance")

if submitted:
    if None in [gender, age_group, living_situation, parent_edu, financial_status, study_hours, extra_tutoring, attendance, motivation, bullying, peer_pressure, parent_meeting, confidence, counseling, foundational_knowledge, department, class_selection] or None in performance.values():
        st.error("Please fill in all required fields before predicting.")
    else:
        input_data = {
            'Gender': gender,
            'Age Group': age_group,
            'Living Situation': living_situation,
            'Parent Education Level': parent_edu,
            'Family Financial Status': financial_status,
            'Class': class_selection,  
            'Department': department,
            'Study Hours per Week': study_hours,
            'Extra Tutoring': extra_tutoring,
            'School Attendance': attendance,
            'Experienced Bullying': bullying,
            'Peer Pressure': peer_pressure,
            'Parents Attend Parent-Teacher Meeting': parent_meeting,
            'Confidence in Academic Ability': confidence,
            'Access to Counseling': counseling,
            'Motivation for Attending School': motivation,
            'Foundational Knowledge': foundational_knowledge
        }
        for subject in subjects:
            input_data[f'Performance in {subject}'] = performance[subject]
        
        prediction = predict_input(model, input_data, categorical_cols, encoder)
        st.success(f"Predicted Performance: {prediction}")
