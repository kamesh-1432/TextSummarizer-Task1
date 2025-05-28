# Import tools needed for the app
from transformers import pipeline  # For summarizing text
import nltk  # For text processing
from nltk.tokenize import sent_tokenize  # To split text into sentences
import streamlit as st  # For creating the web app

# Download NLTK data for sentence splitting
nltk.download('punkt')

# Function to summarize an article
def summarize_text(article):
    # Check if the article is empty or too short (less than 50 words)
    if not article or len(article.split()) < 50:
        return "Error: Please enter an article with at least 50 words."
    
    # Clean the text by removing extra spaces
    article = " ".join(article.split())
    
    # Load the T5-small model for abstractive summarization
    summarizer = pipeline("summarization", model="t5-small")
    
    # Set summary length to 20-30% of the article's length
    max_len = min(400, int(len(article.split()) * 0.3))
    min_len = min(200, int(max_len * 0.5))
    
    # Generate the summary
    summary = summarizer(article, max_length=max_len, min_length=min_len, do_sample=False)
    
    # Return the summary text
    return summary[0]['summary_text']

# Create the Streamlit web app
st.title("Text Summarizer App")  # App title
st.write("Paste a long article below and click Summarize to get a short summary!")  # Instructions

# Text box for users to paste the article
article = st.text_area("Enter your article here:", height=200)

# Button to trigger summarization
if st.button("Summarize"):
    if article:
        # Get the summary using the function
        summary = summarize_text(article)
        # Show the original article
        st.subheader("Original Article:")
        st.write(article)
        # Show the summary
        st.subheader("Summary:")
        st.write(summary)
    else:
        # Show error if no article is entered
        st.write("Please enter an article before clicking Summarize.")
