import streamlit as st

st.title("Checkbox Example")

# Create a dictionary to store the attribute labels and their default values
attributes = {
    "Analytic inquiry": False,
    "Use of information resources": False,
    "Engaging diverse perspectives": False,
    "Ethical reasoning": False,
    "Quantitative fluency": False,
    "Communication fluency": False,
}

# Use a for loop to create a checkbox for each attribute
for key in attributes:
    attributes[key] = st.checkbox(key)

# Print out the selected attributes
selected_attributes = [key for key, value in attributes.items() if value]
st.write("Selected attributes:", selected_attributes)
