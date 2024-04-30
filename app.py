import streamlit as st
import nltk
from newspaper import Article

def main():
  st.write('MCX')
  url = st.text_input('Enter URL Below')

  if url:  # Check if user entered a URL
    article = Article(url)
    article.download()
    article.parse()
    nltk.download('punkt')
    article.nlp()
    with st.container():
      st.write(article.summary)
  else:
    st.write("Please enter a URL to download and process the article.")

if __name__ == "__main__":
  main()
