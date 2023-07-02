# spxing/natural_language_processing/nlu.py

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class NLU:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.user_input = None
        self.knowledge_base = None

    def preprocess_text(self, text):
        words = nltk.word_tokenize(text.lower())
        words = [word for word in words if word.isalpha() and word not in self.stop_words]
        words = [self.lemmatizer.lemmatize(word) for word in words]
        return ' '.join(words)

    def add_to_knowledge_base(self, data):
        if self.knowledge_base is None:
            self.knowledge_base = [data]
        else:
            self.knowledge_base.append(data)

    def set_user_input(self, user_input):
        self.user_input = user_input

    def process_intent(self):
        if not self.knowledge_base:
            raise ValueError("Knowledge base is empty. Please add data to the knowledge base.")

        preprocessed_input = self.preprocess_text(self.user_input)

        # Vectorize the input and the knowledge base
        all_texts = [preprocessed_input] + [self.preprocess_text(data) for data in self.knowledge_base]
        vectors = self.vectorizer.fit_transform(all_texts)
        similarity_scores = cosine_similarity(vectors)

        # Find the most similar data in the knowledge base
        most_similar_index = similarity_scores[0].argsort()[-2]
        most_similar_data = self.knowledge_base[most_similar_index - 1]

        return most_similar_data
