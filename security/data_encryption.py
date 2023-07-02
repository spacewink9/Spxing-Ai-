import base64
from cryptography.fernet import Fernet

class DataEncryption:
    def __init__(self, key=None):
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key

        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        """
        Encrypts the input data using Fernet symmetric encryption.
        :param data: The data to be encrypted.
        :return: Encrypted data as a string.
        """
        encrypted_data = self.cipher.encrypt(data.encode())
        return base64.urlsafe_b64encode(encrypted_data).decode()

    def decrypt(self, encrypted_data):
        """
        Decrypts the input encrypted data using Fernet symmetric encryption.
        :param encrypted_data: The encrypted data to be decrypted (as a string).
        :return: Decrypted data as a string.
        """
        decoded_data = base64.urlsafe_b64decode(encrypted_data)
        decrypted_data = self.cipher.decrypt(decoded_data).decode()
        return decrypted_data

    def change_key(self, new_key):
        """
        Changes the encryption key.
        :param new_key: New key as bytes.
        """
        self.key = new_key
        self.cipher = Fernet(self.key)

    def save_key_to_file(self, file_path):
        """
        Saves the encryption key to a file.
        :param file_path: File path where the key will be saved.
        """
        with open(file_path, 'wb') as file:
            file.write(self.key)

    def load_key_from_file(self, file_path):
        """
        Loads the encryption key from a file.
        :param file_path: File path from which the key will be loaded.
        """
        with open(file_path, 'rb') as file:
            self.key = file.read()
            self.cipher = Fernet(self.key)
