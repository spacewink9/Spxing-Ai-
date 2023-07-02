import unittest
from spxing.natural_language_processing.nlu import NaturalLanguageUnderstanding

class TestNaturalLanguageProcessing(unittest.TestCase):
    def setUp(self):
        self.nlu = NaturalLanguageUnderstanding()

    def test_extract_entities(self):
        text = "Can you book a table for two at an Italian restaurant?"
        entities = self.nlu.extract_entities(text)
        self.assertEqual(entities, {"intent": "book_table", "party_size": 2, "cuisine": "Italian"})

    def test_extract_sentiment(self):
        text = "I absolutely loved the movie!"
        sentiment = self.nlu.extract_sentiment(text)
        self.assertEqual(sentiment, "positive")

    def test_extract_keywords(self):
        text = "Can you give me directions to the nearest coffee shop?"
        keywords = self.nlu.extract_keywords(text)
        self.assertEqual(keywords, ["directions", "nearest", "coffee shop"])

    def test_generate_response(self):
        intent = "weather"
        location = "New York"
        response = self.nlu.generate_response(intent, location)
        self.assertEqual(response, "The weather in New York is currently sunny.")

if __name__ == '__main__':
    unittest.main()
