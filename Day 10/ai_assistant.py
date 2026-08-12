from transformers import pipeline

# Load Hugging Face sentiment model
sentiment_model = pipeline("sentiment-analysis")

# Get user input
sentence = input("Enter a sentence: ")

# Predict sentiment
result = sentiment_model(sentence)

# Display result
print("Sentiment:", result[0]["label"])
print("Confidence:", round(result[0]["score"], 4))