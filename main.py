import tkinter as tk
from tkinter import messagebox
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Download NLTK resources (run this once)
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function for sentiment analysis
def analyze_sentiment(text):
    sentiment_score = analyzer.polarity_scores(text)
    compound_score = sentiment_score['compound']
    
    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment, sentiment_score

# Function to handle the button click
def on_analyze_button_click():
    text = entry.get()  # Get text from the input field
    if not text.strip():  # Check if input is empty
        messagebox.showwarning("Input Error", "Please enter some text for analysis.")
        return
    
    sentiment, score = analyze_sentiment(text)
    result_label.config(text=f"Sentiment: {sentiment}")
    score_label.config(text=f"Sentiment Scores: {score}")

# Creating the main window
root = tk.Tk()
root.title("Sentiment Analysis Tool")

# Create and place widgets
title_label = tk.Label(root, text="Sentiment Analysis Tool", font=("Helvetica", 16))
title_label.pack(pady=10)

entry_label = tk.Label(root, text="Enter Text:", font=("Helvetica", 12))
entry_label.pack(pady=5)

entry = tk.Entry(root, width=50, font=("Helvetica", 12))
entry.pack(pady=10)

analyze_button = tk.Button(root, text="Analyze Sentiment", font=("Helvetica", 12), command=on_analyze_button_click)
analyze_button.pack(pady=10)

result_label = tk.Label(root, text="Sentiment: ", font=("Helvetica", 12))
result_label.pack(pady=5)

score_label = tk.Label(root, text="Sentiment Scores: ", font=("Helvetica", 12))
score_label.pack(pady=5)

# Run the main loop
root.mainloop()
