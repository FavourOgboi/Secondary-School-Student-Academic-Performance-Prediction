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

        if prediction:

            # Recommendation System
            st.write("## 📌 Personalized Recommendations")

            recommendations = []

            # Study Hours
            if study_hours == "Less than 5 hours":
                recommendations.append("📖 Increase your study hours to at least 5-10 hours per week to improve performance.")
            elif study_hours == "5 - 10 hours":
                recommendations.append("📚 Consider increasing study hours beyond 10 hours per week for better results.")
            elif study_hours == "More than 10 hours":
                recommendations.append("✅ Your study hours are good! Ensure they are well-structured and effective.")

            # Living Situation
            if living_situation == "Single parent":
                recommendations.append("💡 Seek additional support from teachers or counselors to bridge any gaps in academic support at home.")
            elif living_situation == "Guardian":
                recommendations.append("🏡 Ensure you communicate any academic challenges with your guardian for better guidance.")

            # School Attendance
            if attendance == "Occasionally":
                recommendations.append("🚀 Improve your school attendance for better understanding of subjects.")
            elif attendance == "Most days":
                recommendations.append("📅 Regular attendance is key! Try not to miss important lessons.")
            elif attendance == "Every day":
                recommendations.append("✅ Great job attending school every day! Stay focused and engaged in lessons.")

            # Confidence in Academic Ability
            if confidence == "Not confident":
                recommendations.append("💪 Build confidence by practicing more, seeking help from teachers, and joining study groups.")
            elif confidence == "Somewhat confident":
                recommendations.append("🔎 Keep improving your skills and test yourself regularly to boost confidence.")
            elif confidence == "Confident":
                recommendations.append("🌟 Keep up the good work! Use your confidence to help others and improve further.")

            # Parental Involvement
            if parent_meeting == "Never":
                recommendations.append("👨‍👩‍👦 Encourage your parents to attend meetings for better involvement in your academics.")
            elif parent_meeting == "Sometimes":
                recommendations.append("📢 Regular parental involvement can help in tracking progress. Discuss your academics at home.")
            elif parent_meeting == "Regularly":
                recommendations.append("✅ Having parents involved is great! Keep them updated on your progress.")

            # Access to Counseling
            if counseling == "No":
                recommendations.append("🗣 Consider seeking guidance from a teacher or mentor to help with academic and personal challenges.")

            # Motivation
            if motivation in ["To meet family expectations", "To avoid being bored at home"]:
                recommendations.append("🎯 Try to develop a personal passion for learning beyond external pressures.")

            # Extra Tutoring
            if extra_tutoring == "No":
                recommendations.append("📚 Consider extra tutoring sessions to strengthen your understanding of subjects.")
            elif extra_tutoring == "Occasionally":
                recommendations.append("📖 More regular tutoring can improve academic performance.")
            elif extra_tutoring == "Regularly":
                recommendations.append("✅ Regular tutoring is great! Stay consistent with your learning.")

            # Bullying Experience
            if bullying == "Frequently":
                recommendations.append("🚨 Seek support from teachers, counselors, or trusted adults if you are experiencing bullying.")
            elif bullying == "Occasionally":
                recommendations.append("🤝 Talk to someone you trust about any bullying incidents and seek guidance.")
            elif bullying == "Never":
                recommendations.append("✅ It’s great that you haven’t experienced bullying. Always stand up for yourself and others.")

            # Peer Pressure
            if peer_pressure == "Frequently":
                recommendations.append("⚠️ Be mindful of peer pressure. Stay true to your goals and don’t be afraid to say no.")
            elif peer_pressure == "Occasionally":
                recommendations.append("🛑 Be cautious of situations that might push you into making bad decisions.")
            elif peer_pressure == "Never":
                recommendations.append("✅ It’s great that you handle peer pressure well. Continue making positive choices.")

            # Final Display
            if recommendations:
                for rec in recommendations:
                    st.write(rec)
            else:
                st.write("✅ Keep up the good work! Stay consistent with your studies and seek continuous improvement.")
                
            st.write("## 📌 Subject-Specific Recommendations")

            subject_recommendations = []

            # Subject Performance Mapping (Every subject has a valid performance)
            math_performance = performance["Maths"]
            english_performance = performance["English"]
            biology_performance = performance["Biology"]
            physics_performance = performance["Physics"]
            chemistry_performance = performance["Chemistry"]
            literature_performance = performance["Lit in English"]
            government_performance = performance["Government"]
            CRS_performance = performance["CRS"]
            commerce_performance = performance["Commerce"]
            accounting_performance = performance["Accounting"]
            economics_performance = performance["Economics"]

            # Science Department Recommendations
            if department == "Science":
                if math_performance in ["Poor", "Fair"]:
                    subject_recommendations.append("📊 Improve your Math skills with extra practice, as it’s crucial for science-related courses.")
                if physics_performance in ["Poor", "Fair"]:
                    subject_recommendations.append("🔬 Strengthen your Physics knowledge, especially if you aim for Engineering or Tech careers.")
                if chemistry_performance in ["Poor", "Fair"]:
                    subject_recommendations.append("⚗️ Chemistry is key in Medicine and Engineering. Consider extra tutoring.")
                if biology_performance in ["Poor", "Fair"]:
                    subject_recommendations.append("🧬 Biology is essential for medical and health-related fields. Revise regularly.")

            # Arts Department Recommendations
            elif department == "Arts":
                if literature_performance in ["Poor", "Fair"]:
                    subject_recommendations.append("📖 Enhance your Literature skills to excel in writing, journalism, and law.")
                if government_performance in ["Poor", "Fair"]:
                    subject_recommendations.append("🏛 Understanding Government is important for politics, law, and public administration.")
                if CRS_performance in ["Poor", "Fair"]:
                    subject_recommendations.append("⛪ CRS helps in moral studies and religious roles. Improve with reading and discussions.")

            # Commerce Department Recommendations
            elif department == "Commerce":
                if accounting_performance in ["Poor", "Fair"]:
                    subject_recommendations.append("💰 Accounting is crucial for business-related fields. Practice calculations and principles.")
                if economics_performance in ["Poor", "Fair"]:
                    subject_recommendations.append("📉 Economics helps in finance and business strategy. Study market trends.")
                if commerce_performance in ["Poor", "Fair"]:
                    subject_recommendations.append("🛍️ Commerce knowledge is key for business success. Understand trade concepts.")

            # General Advice for All Departments
            if english_performance in ["Poor", "Fair"]:
                subject_recommendations.append("📝 English is essential for all fields. Improve writing and communication skills.")

            # Display Recommendations
            if subject_recommendations:
                for rec in subject_recommendations:
                    st.write(rec)
            else:
                st.write("✅ Keep up the good work in all subjects! Continue practicing and seeking improvements.")

    # Footer