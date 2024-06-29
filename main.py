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
    st.image('images/reddit_logo.png', width=65)

with col2:
    st.title('Reddit Sentiment Analyzer')

st.text("A simple web application for analyzing reddit sentiments. Receive immediate feedback \non the sentiment, whether it is positive, negative, or neutral")

#with st.expander('Analyze Text'):
#st.markdown('<h3 style="font-size:24px;">:</h3>', unsafe_allow_html=True)
text = st.text_area('Comment:', placeholder='Input text here')
st.markdown('<p style="font-style: italic; color: gray;">Note: Please note that it may not capture the full context of the comment, especially if it is not in English.</p>', unsafe_allow_html=True)

if text:
    blob = TextBlob(text)
    polarity = round(blob.sentiment.polarity, 2)
    subjectivity = round(blob.sentiment.subjectivity, 2)
    st.write('Polarity: ', polarity)
    st.write('Subjectivity: ', subjectivity)

    if polarity >= 0.5:
        st.markdown('<div style="text-align:center;"><span style="font-size:100px;">😊</span><p style="font-size:24px;">Happy!</p></div>', unsafe_allow_html=True)
    elif polarity <= -0.5:
        st.markdown('<div style="text-align:center;"><span style="font-size:48px;">😞</span><p style="font-size:24px;">Sad!</p></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="text-align:center;"><span style="font-size:48px;">😐</span><p style="font-size:24px;">Neutral!</p></div>', unsafe_allow_html=True)

# pre = st.text_input('Clean Text: ')
# if pre:
#     st.write(cleantext.clean(pre, clean_all=False, extra_spaces=True,
#                             stopwords=True, lowercase=True, numbers=True, punct=True))

# with st.expander('Analyze CSV'):
#     upl = st.file_uploader('Upload file')

#     def score(x):
#         blob1 = TextBlob(x)
#         return blob1.sentiment.polarity

#     def analyze(x):
#         if x >= 0.5:
#             return 'Positive'
#         elif x <= -0.5:
#             return 'Negative'
#         else:
#             return 'Neutral'

#     if upl:
#         df = pd.read_excel(upl)
#         del df['Unnamed: 0']
#         df['score'] = df['tweets'].apply(score)
#         df['analysis'] = df['score'].apply(analyze)
#         st.write(df.head(10))

#         @st.cache
#         def convert_df(df):
#             # IMPORTANT: Cache the conversion to prevent computation on every rerun
#             return df.to_csv().encode('utf-8')

#         csv = convert_df(df)

#         st.download_button(
#             label="Download data as CSV",
#             data=csv,
#             file_name='sentiment.csv',
#             mime='text/csv',
#         )

with st.expander('About the creators', icon='ℹ'):
    st.markdown("""
    This web application was created by a team to achieve a proof of concept, and to experiment with the Streamlit library, aiming to provide a simple and intuitive tool 
    for analyzing sentiments in Reddit comments. We hope you find it useful!

    Feedback or suggestions are welcome.
    """)