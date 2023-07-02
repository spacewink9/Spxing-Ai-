import azure.cognitiveservices.speech as speechsdk

class SpeechRecognizer:
    def __init__(self, subscription_key, region):
        self.subscription_key = subscription_key
        self.region = region
        self.speech_config = speechsdk.SpeechConfig(subscription=self.subscription_key, region=self.region)
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config)

    def recognize_speech(self):
        result = self.speech_recognizer.recognize_once_async().get()
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            return "Speech not recognized. Please try again."
        elif result.reason == speechsdk.ResultReason.Canceled:
            return "Speech recognition canceled."
        else:
            return "Unknown speech recognition error."

    def start_continuous_recognition(self):
        self.speech_recognizer.recognized.connect(lambda evt: self._process_continuous_result(evt))
        self.speech_recognizer.start_continuous_recognition()

    def stop_continuous_recognition(self):
        self.speech_recognizer.stop_continuous_recognition()

    def _process_continuous_result(self, evt):
        result = evt.result
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized speech:", result.text)
            # Perform actions based on recognized speech

