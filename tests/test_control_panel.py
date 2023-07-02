import unittest
from spxing.control_panel import admin_panel, user_profiles, feature_management

class TestControlPanel(unittest.TestCase):
    def setUp(self):
        # Setup test environment if needed
        pass

    def test_admin_login(self):
        # Test the admin login functionality
        admin_panel.login("admin", "admin_password")
        self.assertTrue(admin_panel.is_admin_authenticated())

    def test_user_profile_creation(self):
        # Test user profile creation
        user_profiles.create_profile("john_doe", "john@example.com")
        user_data = user_profiles.get_user_profile("john_doe")
        self.assertEqual(user_data["username"], "john_doe")
        self.assertEqual(user_data["email"], "john@example.com")

    def test_feature_activation(self):
        # Test feature activation and deactivation
        feature_management.activate_feature("weather")
        self.assertTrue(feature_management.is_feature_active("weather"))

        feature_management.deactivate_feature("music")
        self.assertFalse(feature_management.is_feature_active("music"))

    def test_invalid_admin_login(self):
        # Test invalid admin login credentials
        with self.assertRaises(ValueError):
            admin_panel.login("admin", "wrong_password")

    def test_nonexistent_user_profile(self):
        # Test retrieval of a nonexistent user profile
        user_data = user_profiles.get_user_profile("nonexistent_user")
        self.assertIsNone(user_data)

    def test_missing_feature_activation(self):
        # Test activation of a non-existent feature
        with self.assertRaises(ValueError):
            feature_management.activate_feature("nonexistent_feature")

    def test_empty_user_profile_creation(self):
        # Test creation of a user profile with missing information
        with self.assertRaises(ValueError):
            user_profiles.create_profile("", "")

if __name__ == '__main__':
    unittest.main()
