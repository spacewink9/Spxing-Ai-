from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt
import speech_recognition as sr

class SpxingGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spxing AI")
        self.setGeometry(100, 100, 800, 600)  # Set the window position and size
        self.setWindowFlag(Qt.WindowStaysOnTopHint)  # Keep the window on top of others
        self.init_ui()

    def init_ui(self):
        # Create and position the UI elements
        self.label = QLabel("Listening...", self)
        self.label.setGeometry(10, 10, 780, 480)
        self.label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton("Listen", self)
        self.button.setGeometry(10, 500, 780, 90)
        self.button.clicked.connect(self.listen_to_voice)

    def listen_to_voice(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            voice_command = recognizer.recognize_google(audio)
            self.label.setText(voice_command)
            self.process_voice_command(voice_command)
        except sr.UnknownValueError:
            self.label.setText("Sorry, I didn't understand that.")
        except sr.RequestError:
            self.label.setText("Sorry, I'm having trouble accessing the speech recognition service.")

    def process_voice_command(self, command):
        # Implement logic to process the voice command and perform appropriate actions
        if command == "turn on the lights":
            # Code to turn on the lights
            pass
        elif command == "play music":
            # Code to play music
            pass
        elif command == "search the web":
            # Code to perform a web search
            pass
        # ... add more feature implementations here

if __name__ == "__main__":
    app = QApplication([])
    window = SpxingGUI()
    window.showFullScreen()  # Show the window in full-screen mode
    app.exec_()
