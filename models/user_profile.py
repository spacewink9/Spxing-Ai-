# spxing/models/user_profile.py

class UserProfile:
    def __init__(self, user_id):
        # Initialize user profile with user-specific attributes
        self.user_id = user_id
        self.name = None
        self.age = None
        self.location = None
        self.preferences = {}

    def update_profile(self, name=None, age=None, location=None):
        # Update user profile attributes if provided
        if name:
            self.name = name
        if age:
            self.age = age
        if location:
            self.location = location

    def set_preference(self, key, value):
        # Set a preference for the user
        self.preferences[key] = value

    def get_preference(self, key):
        # Get the value of a specific preference
        return self.preferences.get(key)

    def clear_preference(self, key):
        # Clear a specific preference
        if key in self.preferences:
            del self.preferences[key]

    def clear_all_preferences(self):
        # Clear all user preferences
        self.preferences = {}

    def __str__(self):
        # String representation of the user profile
        profile_str = f"User ID: {self.user_id}\nName: {self.name}\nAge: {self.age}\nLocation: {self.location}\n"
        if self.preferences:
            profile_str += "Preferences:\n"
            for key, value in self.preferences.items():
                profile_str += f"{key}: {value}\n"
        return profile_str
