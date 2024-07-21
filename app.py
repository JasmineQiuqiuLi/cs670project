import streamlit as st
from transformers import pipeline

# load the pipeline
sentiment_analysis = pipeline("sentiment-analysis")

# Title of the application
st.title('Welcome to my Streamlit App!')

# Display text
st.write("This is a simple Streamlit application.")

# Display emoji
st.write("Here's an emoji for you: :smiley:")

# A placeholder for additional content
st.write("Use the endpoint /predict to get sentiment analysis results.")

user_input = st.text_input('Enter something:')

if st.button('Submit'):
    if user_input:
        results = sentiment_analysis(user_input)
        st.write('The detected sentiment is', result[0].label, "with a score of",result[0].score)
    else:
        st.write('Please enter something!')
