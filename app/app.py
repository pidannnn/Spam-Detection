import gradio as gr
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# load model
model = joblib.load("../models/svm_model.pkl")
tfidf = joblib.load("../models/tfidf.pkl")

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    tokens = text.split()
    tokens = [stemmer.stem(w) for w in tokens if w not in stop_words]
    return ' '.join(tokens)

def predict(text):
    clean = preprocess(text)
    vec = tfidf.transform([clean]).toarray()
    pred = model.predict(vec)[0]
    
    return "🚨 SPAM" if pred == 1 else "✅ HAM"

app = gr.Interface(
    fn=predict,
    inputs="text",
    outputs="text",
    title="Spam Detection App",
    description="Detect whether message is Spam or Ham"
)

app.launch()