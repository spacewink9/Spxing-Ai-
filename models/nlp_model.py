import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

class NLPModel:
    def __init__(self):
        self.tokenizer = word_tokenize
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = TfidfVectorizer()
        self.classifier = MultinomialNB()
        self.intents = {}
        self.entities = {}

    def preprocess_text(self, text):
        # Tokenize text and remove stopwords
        tokens = [word.lower() for word in self.tokenizer(text) if word.lower() not in stopwords.words("english")]
        # Lemmatize tokens
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        return " ".join(lemmatized_tokens)

    def add_intent(self, intent_name, examples):
        # Add intent with training examples
        processed_examples = [self.preprocess_text(example) for example in examples]
        self.intents[intent_name] = processed_examples

    def add_entity(self, entity_name, examples):
        # Add entity with training examples
        processed_examples = [self.preprocess_text(example) for example in examples]
        self.entities[entity_name] = processed_examples

    def train_classifier(self):
        # Prepare training data and labels
        X_train = []
        y_train = []
        for intent, examples in self.intents.items():
            X_train.extend(examples)
            y_train.extend([intent] * len(examples))
        # Vectorize and train the classifier
        X_train_vectorized = self.vectorizer.fit_transform(X_train)
        self.classifier.fit(X_train_vectorized, y_train)

    def predict_intent(self, text):
        # Predict the intent of user input
        processed_text = self.preprocess_text(text)
        X_test_vectorized = self.vectorizer.transform([processed_text])
        intent = self.classifier.predict(X_test_vectorized)[0]
        return intent

    def add_entity_to_text(self, text, entity_name, entity_value):
        # Replace entity placeholders in text with the actual entity value
        return text.replace(f"{{{entity_name}}}", entity_value)

    def extract_entities(self, text):
        # Extract entities from user input
        entities = {}
        for entity_name, examples in self.entities.items():
            for example in examples:
                if example in text:
                    entities[entity_name] = example
                    break
        return entities
