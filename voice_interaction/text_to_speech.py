import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def set_voice(self, voice_id):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voice_id].id)

    def set_rate(self, rate):
        self.engine.setProperty('rate', rate)

    def set_volume(self, volume):
        self.engine.setProperty('volume', volume)

# Usage example
if __name__ == "__main__":
    tts = TextToSpeech()
    tts.set_voice(0)  # Set voice index
    tts.set_rate(150)  # Set speech rate (words per minute)
    tts.set_volume(1.0)  # Set volume level

    text = "Hello, I am Spxing, your AI assistant. How can I assist you today?"
    tts.speak(text)
