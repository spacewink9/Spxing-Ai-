# spxing/models/joke_service.py

import random

class JokeService:
    def __init__(self):
        # Initialize the joke service with a list of jokes and categories
        self.jokes = []
        self.categories = set()

    def add_joke(self, joke, category=None):
        # Add a joke to the joke service with an optional category
        self.jokes.append((joke, category))
        if category:
            self.categories.add(category)

    def get_random_joke(self, category=None):
        # Get a random joke from the joke service, optionally filtered by category
        if category and category not in self.categories:
            raise ValueError(f"Category '{category}' not found in joke service.")

        filtered_jokes = [joke for joke, joke_category in self.jokes if joke_category == category]
        if not filtered_jokes:
            if category:
                raise ValueError(f"No jokes found for category '{category}'.")
            else:
                raise ValueError("No jokes found in the joke service.")
        
        return random.choice(filtered_jokes)

    # Rest of the class code remains unchanged

if __name__ == "__main__":
    # Example usage of the JokeService class
    joke_service = JokeService()
    joke_service.add_joke("Why don't scientists trust atoms? Because they make up everything.", category="Science")
    joke_service.add_joke("Why was the math book sad? Because it had too many problems.", category="Math")
    joke_service.add_joke("Why did the scarecrow win an award? Because he was outstanding in his field!", category="Puns")

    try:
        random_joke = joke_service.get_random_joke()
        print("Random Joke:", random_joke)

        science_joke = joke_service.get_random_joke(category="Science")
        print("Science Joke:", science_joke)

        all_categories = joke_service.get_all_categories()
        print("All Categories:", all_categories)

        combination_joke = joke_service.generate_combination_joke(["banana", "apple", "orange", "grape"])
        print("Combination Joke:", combination_joke)

    except ValueError as e:
        print("Error:", str(e))
