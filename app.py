import streamlit as st
from transformers import pipeline

# load the pipeline
sentiment_analysis = pipeline("sentiment-analysis")

# title
st.title('Analyze Sentiment of Text!')

# Display text
st.write("You will get a sentiment analysis after you enter something.")

# show an emoji
st.write("Let's try it: :smiley:")

user_input = st.text_input('Enter something below:')

if st.button('Submit'):
    if user_input:
        results = sentiment_analysis(user_input)
        st.write('The detected sentiment is', result[0].label, "with a score of",result[0].score)
    else:
        st.write('Please enter something!')
