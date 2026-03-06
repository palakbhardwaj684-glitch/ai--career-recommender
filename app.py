import streamlit as st
import pandas as pd
import random
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

career_roadmap = {
"Data Scientist": [
"Learn Python",
"Learn Statistics",
"Learn Machine Learning",
"Practice Data Visualization",
"Build Data Science Projects"
],

"Web Developer": [
"Learn HTML CSS",
"Learn JavaScript",
"Learn React",
"Build Websites",
"Deploy Projects"
],

"AI Engineer": [
"Learn Python",
"Learn Machine Learning",
"Learn Deep Learning",
"Work with TensorFlow",
"Build AI Projects"
],

"Accountant": [
"Learn Accounting Basics",
"Learn Taxation",
"Practice Excel",
"Understand Financial Statements",
"Use Accounting Software"
],

"Digital Marketer": [
"Learn Social Media Marketing",
"Learn SEO",
"Learn Content Marketing",
"Run Ads Campaign",
"Analyze Marketing Data"
]

}


career_explanation = {
"Data Scientist": [
"Data Scientists analyze data using machine learning and statistics to find insights.",
"They work with large datasets and build predictive models for companies."
],

"Web Developer": [
"Web Developers build websites and web applications using programming languages.",
"They design user interfaces and ensure websites work smoothly."
],

"AI Engineer": [
"AI Engineers develop artificial intelligence systems using machine learning and deep learning.",
"They build smart applications like chatbots and recommendation systems."
],

"Accountant": [
"Accountants manage financial records, taxation and company budgets.",
"They help businesses track income, expenses and financial performance."
],

"Digital Marketer": [
"Digital Marketers promote products using online platforms like social media and search engines.",
"They use marketing strategies to grow business online."
]
}
df = pd.DataFrame(data)

st.set_page_config(page_title="AI Career Path Recommender", page_icon="🎯")
st.title("🎯 AI Career Recommender")
st.write("This AI tool recommends the best career based on your skills using machine learning.")
user_input=st.text_area("Your Skills (comma separated)", "Python, Statistics, HTML")

if st.button("Find Careers"):
    vectorizer = TfidfVectorizer()
    skill_matrix = vectorizer.fit_transform(df["Required_Skills"])

    user_vector = vectorizer.transform([user_input])

    similarity_scores = cosine_similarity(user_vector,skill_matrix).flatten()

    df["Match_Score"] = similarity_scores

    df["Match_Score"] = df["Match_Score"] * 100
    df["Match_Score"] = df["Match_Score"].round(2)

    recommendations = df.sort_values(by="Match_Score", ascending=False).head(3)
    top_career = recommendations.iloc[0]["Career"]

    st.sucess(f"Best Career Recommendation: {top_career}")
    
    st.subheader("🗺️ Career Roadmap")

    if top_career in career_roadmap:
       for step in career_roadmap[top_career]:
    st.write("•" + step)
    st.subheader("🤖 AI Career Insight")

if top_career in career_explanation:
    st.write(random.choice(career_explanation[top_career]))
    st.subheader("🔮 Recommended Careers")
    st.table(recommendations[["Career", "Match_Score"]])

    user_skills = set([s.strip().lower() for s in user_input.split(",")])

    for _, row in recommendations.iterrows():
        career = row["Career"]
        required_skills = set([s.strip().lower() for s in row["Required_Skills"].split(",")])
        missing_skills = required_skills - user_skills

        st.write(f"**{career}** → Missing Skills: {', '.join(missing_skills) if missing_skills else 'None 🎉'}")
        st.markdown("---")
        st.write("Developed by palak | AI Career Advisor Project")
