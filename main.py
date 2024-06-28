from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext

st.header('Reddit Comment Sentiment Analyzer')
with st.expander('Analyze Text'):
    text = st.text_input('Input text here: ')
    if text:
        blob = TextBlob(text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
