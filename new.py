import streamlit as st

def main():
    st.title("Transferable Skills and Applications Form")

    # Intellectual Skills Section
    st.header("What degree-based skills do you have?")
    st.write("Please select your top transferable intellectual skills:")
    intellectual_skills_options = ["Analytic Inquiry", "Use of Information and Resources", 
                                  "Engaging Diverse Perspectives", "Ethical Reasoning", 
                                  "Quantitative Fluency", "Communication Fluency"]
    intellectual_skills = st.multiselect("Intellectual Skills", intellectual_skills_options)

    # Applied and Collaborative Learning Section
    st.header("Applied and Collaborative Learning")
    st.write("Please describe any practical applications or examples of how you have used your intellectual skills in a collaborative or applied setting:")
    applied_learning = st.text_area("Applied and Collaborative Learning")

    # Civic and Global Learning Section
    st.header("Civic and Global Learning")
    st.write("Please describe any experiences or examples of how you have applied your intellectual skills to civic or global issues:")
    civic_learning = st.text_area("Civic and Global Learning")

    # Submit Button
    if st.button("Submit"):
        # Store the responses in a dictionary
        responses = {
            "intellectual_skills": intellectual_skills,
            "applied_learning": applied_learning,
            "civic_learning": civic_learning
        }
        # Print the responses to the console
        print(responses)

if __name__ == "__main__":
    main()
