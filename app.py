import streamlit as st

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
    # This code runs when the button is clicked
    if user_input:
        st.write('You entered:', user_input)
    else:
        st.write('Please enter something!')
