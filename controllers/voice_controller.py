from voice.listener import listen


class VoiceController:

    def listen_once(self):

        print("🎤 Listening...")

        text = listen()

        return text