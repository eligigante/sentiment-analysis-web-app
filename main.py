from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext

def get_sentiment_emoji(sentiment):
    if sentiment == 'Positive':
        return '😃'
    elif sentiment == 'Negative':
        return '😞'
    else:
        return '😐'

col1, col2 = st.columns([1, 9])

with col1:
    st.write("")
    st.image('images/reddit_logo.png', width=65)  # Adjust width as needed

with col2:
    st.title('Reddit Sentiment Analyzer')

st.text("A simple web application for analyzing reddit sentiments. Receive immediate feedback \non the sentiment, whether it is positive or negative")

with st.expander('Analyze Text'):
    text = st.text_input('Input text here: ')
    if text:
        blob = TextBlob(text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)
        st.write('Polarity: ', polarity)
        st.write('Subjectivity: ', subjectivity)

        if polarity >= 0.5:
            st.write('Sentiment: Positive', get_sentiment_emoji('Positive'))
        elif polarity <= -0.5:
            st.write('Sentiment: Negative', get_sentiment_emoji('Negative'))
        else:
            st.write('Sentiment: Neutral', get_sentiment_emoji('Neutral'))

    pre = st.text_input('Clean Text: ')
    if pre:
        st.write(cleantext.clean(pre, clean_all=False, extra_spaces=True,
                                 stopwords=True, lowercase=True, numbers=True, punct=True))

with st.expander('Analyze CSV'):
    upl = st.file_uploader('Upload file')

    def score(x):
        blob1 = TextBlob(x)
        return blob1.sentiment.polarity

    def analyze(x):
        if x >= 0.5:
            return 'Positive'
        elif x <= -0.5:
            return 'Negative'
        else:
            return 'Neutral'

    if upl:
        df = pd.read_excel(upl)
        del df['Unnamed: 0']
        df['score'] = df['tweets'].apply(score)
        df['analysis'] = df['score'].apply(analyze)
        st.write(df.head(10))

        @st.cache
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='sentiment.csv',
            mime='text/csv',
        )
