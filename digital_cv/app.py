from pathlib import Path
import altair as alt
import streamlit as st
from PIL import Image


#--- PATH SETTINGS---
current_dir = Path(__file__).parent if "__file__" in locals()else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_Shefali.pdf"
profile_pic= current_dir / "assets" / "shef-profile-pic.png"



#--GENERAL SETTINGS---

PAGE_TITLE = "Digital CV | Shefali Chaugule"
PAGE_ICON = ":globe_with_meridians:"
NAME = "Shefali Chaugule"
DESCRIPTION = """Python | Machine Learning | Data driven decision making. """
EMAIL = "Chauguleshefali9867@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/shefali-chaugule-942789200/",
    "GitHub": "https://github.com/Shefali9867",
}
PROJECTS = {
    "🏆 A Boosting Technique for Diabetes Mellitus Classification and Prediction in the Healthcare Industry Based on Machine Learning Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 A Machine Learning Framework for Domain Generation Algorith(DGA)Based Malware Detection": "https://youtu.be/3egaMfE9388",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write("---")
st.write(
    """
- ✔️ Expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL,Java,JavaScript,CSS.
- 📊 Data Visulization:  MS Excel, Plotly, Tableau
- 📚 Modeling: Logistic regression, Linear regression, decision trees,Supervised-Unsupervised Learning Techniques.
- 🗄️ Databases:  MongoDB, MySQL
"""
)

st.write('\n')
st.subheader("Soft Skills")
st.write("---")
st.write(
    """
- ✔️Problem Solving, Critical Thinking
- ✔️Leadership, Collaboration, Teamwork
- ✔️ Enthusiasm for Data Interpretation
    """

)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Tesco Stock Control Colleague | Tesco LTD**")
st.write("10/2022 - Present")
st.write(
    """
- ► Maintain accurate records of stock levels, ensuring adequate supply without overstocking
- ► Maintain meticulous records and enter data accurately into inventory management systems. Generate reports to track stock movements and trends.
- ► Implement FIFO (First In, First Out) method to ensure older stock is used first, reducing waste.
"""
)

#---CERTIFICATIONS---
st.write('\n')
st.subheader("CERTIFICATIONS")
st.write("---")



# --- Projects ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


















