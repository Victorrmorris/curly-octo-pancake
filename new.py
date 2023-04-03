import streamlit as st

st.title("Analytic Inquiry")

topic = st.selectbox("Select a topic", ["Identify and frame a problem or question", "Distinguish among ideas concepts, theories or practical approaches to the problem"])

if topic == "Identify and frame a problem or question":
    st.write("You have selected 'Identify and frame a problem or question' topic.")
elif topic == "Distinguish among ideas concepts, theories or practical approaches to the problem":
    st.write("You have selected 'Distinguish among ideas concepts, theories or practical approaches to the problem' topic.")
