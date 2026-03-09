
# AI Career Recommender 🎯

This project recommends the best career based on a user's skills using Machine Learning.

Working App:
"https://ai--career-recommender-zwtqgfyibptxvcck5s8yce.streamlit.app/"
-----
Features
• Career recommendation based on user skills  
• Machine Learning based similarity matching  
• Career roadmap guidance  
• AI career insights  
• Missing skills analysis  
• Interactive web interface using Streamlit  

---
 How it Works
The system analyzes the user's skills and compares them with required skills for different careers.
The recommendation is generated using:
1️⃣ TF-IDF Vectorization  
2️⃣ Cosine Similarity Matching  
3️⃣ Skill comparison with career datasets  

The system then:

• Finds the best matching career  
• Shows top career recommendations  
• Displays a learning roadmap  
• Suggests missing skills

---

 Technologies Used

Python  
Streamlit  
Pandas  
Scikit-Learn  
Machine Learning (TF-IDF + Cosine Similarity)

---

 Run Locally

Install dependencies:
pip install streamlit pandas
scikit-learn

Run the app:
streamlit run app.py
