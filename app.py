from pathlib import Path
from PIL import Image
import os
import streamlit as st

current_dir = Path.cwd()
# construct the path of assets and other files based on the parent (main) directory.
cv_file = os.path.join(current_dir, 'assets', 'cv.pdf')
css_file = os.path.join(current_dir, 'styles', 'main.css')
profile_pic_file = os.path.join(current_dir, 'assets', 'pic.jpg')
# print(cv_file,css_file) # to test

PAGE_TITLE = 'Digital Resume - Sreenivas Pakyala'
ICON = '👨‍💼'
NAME = 'Sreenivas Pakyala'
DESCRIPTION = """
Machine Learning Associate, assisting businees in developing Predictive Models.    
"""
EMAIL = 'pakyalasreenivas@gmail.com'

SOCIAL_LINKS = {
    'Github' : 'https://github.com/sreenivaspakyala',
    'Linkedin' : 'https://www.linkedin.com/in/sreenivas-pakyala/'
}

st.set_page_config(page_title=PAGE_TITLE, page_icon= ICON)

st.header('Hi !👋 This is the begining of my Digital Resume...')

with open(css_file, 'r') as css:
    st.markdown('<style>{}</style>'.format(css.read()), unsafe_allow_html=True)

with open(cv_file, 'rb') as cv:
    pdf_bytes = cv.read()

profile_pic = Image.open(profile_pic_file)

# create sections in the streamlit webpage

col1, col2 = st.columns(2)

with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = '📄 Download Resume',
        data = pdf_bytes,
        file_name = 'sreenivas_pakyala_resume.pdf',
        mime = 'application/octet-stream'
    )
    st.write('📧 ', EMAIL)

st.write('#')

cols = st.columns(len(SOCIAL_LINKS))
for idx, (site, link) in enumerate(SOCIAL_LINKS.items()):
    cols[idx].write(f'[{site}]({link})')

st.write('#')
# now let's write down experience and qualifications
st.subheader('Experience & Qualifications')
st.write(
    """
- 🎯2+ years of Experience in building machine Learning Models.
- 🎯Strong hands on experince in Python, SQL and Azure Databricks.
- 🎯Experience in developing ETL pipelines and SQL to extract data.
- 🎯Experience in building predictive models using Time series data.
- 🎯Experience in Implementing an ML model End-to-End including deployment.
"""
)

st.write('#')
# now let's write down certifications.
st.subheader('Certifications')
st.write(
    """
- 💎Azure AI Engineer Associate.
- 💎Google Associate cloud Engineer.
- 💎Python certified Associate Programmer.

"""
)

st.write('#')
# now let's write down skills.
st.subheader('Skills')
st.write(
    """
- 👌Programming: Python, SQL, PySpark
- 👌Frameworks: Pandas, Scikit-learn, Tensorflow, Streamlit 
- 👌Cloud: Azure, GCP, Databricks
- 👌Technologies: Machine Learning, Deep Learning, ETL
- 👌Databases: Oracle SQL, MySQL
"""
)

st.write('#')
# now let's write down work experience.
st.subheader('Work Experience')
st.write(
    """
- ▶ Programming: Python, SQL, PySpark
- ▶ Frameworks: Pandas, Scikit-learn, Tensorflow, Streamlit 
- ▶ Cloud: Azure, GCP, Databricks
- ▶ Technologies: Machine Learning, Deep Learning, ETL
- ▶ Databases: Oracle SQL, MySQL
"""
)

st.write('#')
# now let's write down projects.
st.subheader('Projects & Accomplishments')
st.write(
    """
- 🏆Programming: Python, SQL, PySpark
- 🏆Frameworks: Pandas, Scikit-learn, Tensorflow, Streamlit 
- 🏆Cloud: Azure, GCP, Databricks
- 🏆Technologies: Machine Learning, Deep Learning, ETL
- 🏆Databases: Oracle SQL, MySQL
"""
)
