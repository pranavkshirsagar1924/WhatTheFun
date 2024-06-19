import pandas as pd
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset
dataset_url = 'Dynamically Generated Hate Dataset v0.2.2.csv'
df = pd.read_csv(dataset_url)

# Display the first few rows
print(df.head())

# Download stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

# Preprocess text function
def preprocess_text(text):
    words = nltk.word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return " ".join(words)

# Apply preprocessing to the dataset
df['clean_text'] = df['text'].apply(preprocess_text)

# Feature extraction using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['clean_text'])
y = df['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Function to predict NSFW content
def predict_nsfw(text):
    clean_text = preprocess_text(text)
    text_vector = vectorizer.transform([clean_text])
    prediction = model.predict(text_vector)
    return "NSFW" if prediction[0] == "hate" else "Safe"

# Example usage in a loop

