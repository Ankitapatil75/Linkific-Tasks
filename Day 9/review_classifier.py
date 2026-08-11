import joblib

# Load the trained vectorizer and model
vectorizer = joblib.load("tfidf_vectorizer.pkl")
classifier = joblib.load("sentiment_model.pkl")

# Get movie review from user
review = input("Enter a movie review: ")

# Convert review into TF-IDF features
review_tfidf = vectorizer.transform([review])

# Predict sentiment
prediction = classifier.predict(review_tfidf)

# Display result
if prediction[0] == 1:
    print("Positive")
else:
    print("Negative")