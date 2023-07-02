# user_profiles.py

class UserProfile:
    def __init__(self, user_id, name, age, interests=None):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.interests = interests if interests else []

    def add_interest(self, interest):
        self.interests.append(interest)

    def remove_interest(self, interest):
        if interest in self.interests:
            self.interests.remove(interest)

    def update_profile(self, name=None, age=None):
        if name:
            self.name = name
        if age:
            self.age = age

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "age": self.age,
            "interests": self.interests
        }

class UserProfilesManager:
    def __init__(self):
        self.profiles = {}

    def create_profile(self, user_id, name, age, interests=None):
        profile = UserProfile(user_id, name, age, interests)
        self.profiles[user_id] = profile

    def get_profile(self, user_id):
        return self.profiles.get(user_id)

    def update_profile(self, user_id, name=None, age=None):
        profile = self.get_profile(user_id)
        if profile:
            profile.update_profile(name, age)

    def add_interest(self, user_id, interest):
        profile = self.get_profile(user_id)
        if profile:
            profile.add_interest(interest)

    def remove_interest(self, user_id, interest):
        profile = self.get_profile(user_id)
        if profile:
            profile.remove_interest(interest)

    def delete_profile(self, user_id):
        if user_id in self.profiles:
            del self.profiles[user_id]

    def get_all_profiles(self):
        return list(self.profiles.values())

    def save_profiles_to_file(self, filename):
        with open(filename, 'w') as f:
            for profile in self.profiles.values():
                f.write(f"{profile.to_dict()}\n")

    def load_profiles_from_file(self, filename):
        with open(filename, 'r') as f:
            data = f.read()
            profiles_data = eval(data)  # WARNING: This is not safe, consider using JSON or other safer serialization.
            for profile_data in profiles_data:
                profile = UserProfile(profile_data["user_id"], profile_data["name"], profile_data["age"], profile_data["interests"])
                self.profiles[profile_data["user_id"]] = profile
