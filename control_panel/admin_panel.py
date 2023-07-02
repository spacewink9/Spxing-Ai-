from flask import Flask, render_template, request, redirect
from control_panel.user_profiles import UserProfiles
from control_panel.feature_management import FeatureManagement

app = Flask(__name__)

# Initialize UserProfiles and FeatureManagement
user_profiles = UserProfiles()
feature_management = FeatureManagement()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/profile', methods=['GET', 'POST'])
def user_profile():
    if request.method == 'POST':
        # Handle user profile update
        username = request.form['username']
        preferences = request.form.getlist('preferences')

        user_profiles.update_profile(username, preferences)
        return redirect('/user/profile')

    # Display user profile form
    user_list = user_profiles.get_user_list()
    return render_template('user_profile.html', user_list=user_list)

@app.route('/feature/manage', methods=['GET', 'POST'])
def manage_features():
    if request.method == 'POST':
        # Handle feature management
        feature = request.form['feature']
        action = request.form['action']

        if action == 'add':
            feature_management.add_feature(feature)
        elif action == 'remove':
            feature_management.remove_feature(feature)

        return redirect('/feature/manage')

    # Display feature management form
    available_features = feature_management.get_available_features()
    active_features = feature_management.get_active_features()
    return render_template('manage_features.html', available_features=available_features, active_features=active_features)

if __name__ == '__main__':
    app.run()
