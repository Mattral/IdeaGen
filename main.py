import streamlit as st

from model import GeneralModel


    
    
def app():
    # Creating an object of prediction service
    pred = GeneralModel()

    api_key = st.sidebar.text_input("APIkey", type="password")
    
    
    
    

    # Using the streamlit cache
    @st.cache
    def process_prompt(inp):

        return pred.model_prediction(inp=inp.strip(), api_key=api_key)

    if api_key:
        st.title("Envisage with me")

        s_example = "What's on your mind?"
        inp = st.text_area(
            "Generate Idea about ",
            value=s_example,
            max_chars=150,
            height=100,
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(inp)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")
