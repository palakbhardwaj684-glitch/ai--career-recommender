import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "Career": [
        "Data Scientist", 
        "Web Developer",
        "AI Engineer",
        "UI/UX Designer", 
        "HR Manager",
        "Accountant",
        "Digital Marketer"],
    "Required_Skills": ["Python, Statistics, Machine Learning, Data Visualization",
        "HTML, CSS, JavaScript, React",
        "Python, Deep Learning, NLP, TensorFlow",
        "Design Thinking, Figma, UX Research, Creativity",
        "Communication,Leadership,Recruitment,People Mangement",
        "Accounting,Finance,Excel,Taxation",
        "Marketing,Social Media,SEO,Communication"]
}

df = pd.DataFrame(data)

st.title("🎯 AI Career Advisor")
st.write("Enter your skills & interests to get career recommendations!")
user_input=st.text_area("Your Skills (comma separated)", "Python, Statistics, HTML")

if st.button("Find Careers"):
    vectorizer = TfidfVectorizer()
    skill_matrix = vectorizer.fit_transform(df["Required_Skills"])

    user_vector = vectorizer.transform([user_input])

    similarity_scores = cosine_similarity(user_vector,skill_matrix).flatten()

    df["Match_Score"] = similarity_scores

    recommendations = df.sort_values(by="Match_Score", ascending=False).head(3)

    st.subheader("🔮 Recommended Careers")
    st.table(recommendations[["Career", "Match_Score"]])

    user_skills = set([s.strip().lower() for s in user_input.split(",")])

    for _, row in recommendations.iterrows():
        career = row["Career"]
        required_skills = set([s.strip().lower() for s in row["Required_Skills"].split(",")])
        missing_skills = required_skills - user_skills

        st.write(f"**{career}** → Missing Skills: {', '.join(missing_skills) if missing_skills else 'None 🎉'}")
