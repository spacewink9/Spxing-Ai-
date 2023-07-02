import unittest
from unittest.mock import patch
from voice_interaction import speech_recognition, text_to_speech, emotion_analysis

class VoiceInteractionTest(unittest.TestCase):
    def test_speech_recognition(self):
        with patch('spxing.voice_interaction.speech_recognition.record_audio') as mock_record_audio:
            # Simulate audio input
            mock_record_audio.return_value = "Hello, Spxing"

            recognized_text = speech_recognition.process_speech()

            self.assertEqual(recognized_text, "Hello, Spxing")

    def test_text_to_speech(self):
        with patch('spxing.voice_interaction.text_to_speech.play_audio') as mock_play_audio:
            # Simulate text input
            text_to_speech.convert_text("Hello, Spxing")

            # Verify that the audio is played
            mock_play_audio.assert_called_with("Hello, Spxing")

    def test_emotion_analysis(self):
        with patch('spxing.voice_interaction.emotion_analysis.analyze_emotion') as mock_analyze_emotion:
            # Simulate emotion analysis
            mock_analyze_emotion.return_value = "Happy"

            emotion = emotion_analysis.detect_emotion("I'm feeling great")

            self.assertEqual(emotion, "Happy")

if __name__ == '__main__':
    unittest.main()
