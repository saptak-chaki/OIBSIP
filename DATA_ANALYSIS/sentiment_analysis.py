import pandas as pd
import numpy as np

# 1. Sample Customer Reviews Dataset
reviews_data = {
    'ReviewID': [1, 2, 3, 4, 5, 6],
    'ReviewText': [
        "Absolutely love this product! Amazing quality and fast delivery.",
        "Worst experience ever. The item broke down on the second day.",
        "It's okay, nothing extraordinary. Works as expected.",
        "Extremely satisfied with the customer support and product performance.",
        "Terrible quality, waste of money. Do not buy!",
        "Pretty good product for the price. Highly recommended."
    ]
}

df_reviews = pd.DataFrame(reviews_data)

# 2. Simple Rule-Based Sentiment Scoring Function
def analyze_sentiment(text):
    text_lower = text.lower()
    positive_words = ['love', 'amazing', 'fast', 'satisfied', 'good', 'recommended', 'support']
    negative_words = ['worst', 'broke', 'terrible', 'waste', 'not']
    
    pos_score = sum(1 for word in positive_words if word in text_lower)
    neg_score = sum(1 for word in negative_words if word in text_lower)
    
    if pos_score > neg_score:
        return 'Positive'
    elif neg_score > pos_score:
        return 'Negative'
    else:
        return 'Neutral'

# 3. Applying Sentiment Analysis
df_reviews['Sentiment'] = df_reviews['ReviewText'].apply(analyze_sentiment)

print("--- Customer Review Sentiment Analysis Results ---")
print(df_reviews[['ReviewText', 'Sentiment']])

# Summary counts
sentiment_counts = df_reviews['Sentiment'].value_counts()
print("\n--- Sentiment Distribution ---")
print(sentiment_counts)