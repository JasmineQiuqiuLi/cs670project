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
        result = sentiment_analysis(user_input)
        st.write('You entered:', result)
    else:
        st.write('Please enter something!')
