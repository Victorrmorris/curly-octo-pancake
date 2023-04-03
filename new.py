import streamlit as st

# Define the list of intellectual skills categories
intellectual_skills = [
    "Analytic inquiry",
    "Use of information resources",
    "Engaging diverse perspectives",
    "Ethical reasoning",
    "Quantitative fluency",
    "Communication fluency"
]

# Display a multiselect widget for users to choose the datapoints
selected_skills = st.sidebar.multiselect(
    "Select intellectual skills categories:",
    intellectual_skills
)

# Display the selected datapoints
st.write("You have selected the following intellectual skills categories:")
for skill in selected_skills:
    st.write("- " + skill)
