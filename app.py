import streamlit as st
from transformers import pipeline

# title
st.title('Analyze Sentiment of Text!')

# Display text
st.write("You will get a sentiment analysis after you enter something.")

# show an emoji
st.write("Let's try it: :smiley:")

user_input = st.text_input('Enter something below:')

model_options = ["finiteautomata/bertweet-base-sentiment-analysis", 
                 "nlptown/bert-base-multilingual-uncased-sentiment", 
                 "bhadresh-savani/distilbert-base-uncased-emotion"]
selected_model = st.selectbox('Choose a model:', model_options)

def choose_model(option):
    chosen_model = pipeline("sentiment-analysis", model=option)
    return chosen_model

# Initialize the model
model = None
if selected_model:
    model = choose_model(selected_model)

if st.button('Submit'):
    if user_input:
        if model:
            results = model(user_input)
            st.write('The detected sentiment is', results[0]['label'], "with a score of", results[0]['score'])
        else:
            st.write('Please select a model!')
    else:
        st.write('Please enter something!')
