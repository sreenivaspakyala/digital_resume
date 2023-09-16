from pathlib import Path
from PIL import Image
import os
import streamlit as st

current_dir = Path.cwd()
# construct the path of assets and other files based on the parent (main) directory.
cv_file = os.path.join(current_dir, 'assets', 'cv.pdf')
css_file = os.path.join(current_dir, 'styles', 'main.css')
profile_pic_file = os.path.join(current_dir, 'assets', 'pic.png')
# print(cv_file,css_file) # to test

PAGE_TITLE = 'Digital Resume - Sreenivas Pakyala'
ICON = '👨‍💼'
NAME = 'Sreenivas Pakyala'
DESCRIPTION = """
Machine Learning Associate, experinece in developing statistical and deep learning models.    
"""
EMAIL = 'pakyalasreenivas@gmail.com'

SOCIAL_LINKS = {
    'Github' : 'https://github.com/sreenivaspakyala',
    'Linkedin' : 'https://www.linkedin.com/in/sreenivas-pakyala/'
}

PROJECTS = {
    'End-to-End Machine Learning project - Using Python, Machine Learning & Docker' : 'https://github.com/sreenivaspakyala/End_To_End_ML_Project',
    'Movie Recommender System - Using Python & Streamlit' : 'https://github.com/sreenivaspakyala/movie_recommender_system',
    'Car Resale value Predictor - Using Python & Machine Learning' : 'https://github.com/sreenivaspakyala/car_resale_value_prediction'
}

st.set_page_config(page_title=PAGE_TITLE, page_icon= ICON)

st.header('Hi !👋 Welcome to my Digital Resume...')

with open(css_file, 'r') as css:
    st.markdown('<style>{}</style>'.format(css.read()), unsafe_allow_html=True)

with open(cv_file, 'rb') as cv:
    pdf_bytes = cv.read()

profile_pic = Image.open(profile_pic_file)

# create sections in the streamlit webpage

col1, col2 = st.columns(2)

with col1:
    st.image(profile_pic, width=300)

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

# st.write('#')
st.write('&nbsp;')

cols = st.columns(len(SOCIAL_LINKS))
for idx, (site, link) in enumerate(SOCIAL_LINKS.items()):
    cols[idx].write(f'[🔗 {site}]({link})')

# st.write('#')
st.write('&nbsp;')
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

# st.write('#')
st.write('&nbsp;')  # to create an empty line
# now let's write down certifications.
st.subheader('Certifications')
st.write(
    """
- 💎Azure AI Engineer Associate.
- 💎Google Associate cloud Engineer.
- 💎Python certified Associate Programmer.

"""
)

# st.write('#')
st.write('&nbsp;')
# now let's write down skills.
st.subheader('Skills')
st.write(
    """
- ◈ Programming: Python, SQL, PySpark
- ◈ Frameworks: Pandas, Scikit-learn, Tensorflow, Streamlit 
- ◈ Cloud: Azure, GCP, Databricks
- ◈ Technologies: Machine Learning, Deep Learning, Docker, ETL
- ◈ Databases: Oracle SQL, MySQL
"""
)
# symbols ⇛▶◉◈
# st.write('#')
st.write('&nbsp;')
st.write('---')
# st.write('#')

# now let's write down work experience.
st.subheader('Work Experience')
st.write('🏁', '**Associate | PricewaterhouseCoopers Ltd.**')
st.write('08/2021 - Present')
st.write(
    """
- ◉ Used Time series models like ARIMA, SARIMA, fbptophet and also Neural Networks using LSTM in
creating Inventory prediction models.
- ◉ Developed a clustering model POC in segregating Customer Churn Problem on Telecom data.
- ◉ Built a Dynamic Price calculator Engine using Machine Learning for a Hardware Manufacture client.
- ◉ Implemented ETL workflows and SQL queries to extract the data for data conversion
"""
)


# st.write('#')
st.write('&nbsp;')
# now let's write down projects.
st.subheader('Projects & Accomplishments')
for project, link  in PROJECTS.items():
    st.write(f'- [⇛ {project}]({link})')

# st.write('#')
