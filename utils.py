import datetime
import os

def get_current_time():
    """
    Get the current time in a specific format.
    """
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def create_directory(path):
    """
    Create a directory at the specified path if it doesn't exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)

def save_to_file(data, file_path):
    """
    Save data to a file at the specified file path.
    """
    with open(file_path, "w") as file:
        file.write(data)

def load_from_file(file_path):
    """
    Load data from a file at the specified file path.
    """
    with open(file_path, "r") as file:
        data = file.read()
    return data

def remove_file(file_path):
    """
    Remove a file at the specified file path.
    """
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} removed successfully.")
    else:
        print(f"File {file_path} does not exist.")

def calculate_similarity(text1, text2):
    """
    Calculate the similarity between two texts.
    """
    # Implement your similarity calculation logic here
    similarity_score = 0.0
    return similarity_score

# Additional utility functions can be added here

