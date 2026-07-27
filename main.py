from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import speech_recognition as sr
import threading

class JarvixMobileUI(BoxLayout):
    def init(self, **kwargs):
        super().init(orientation='vertical', **kwargs)
        self.add_widget(Label(text="JARVIX AI", font_size='28sp', color=(0, 1, 0, 1), size_hint=(1, 0.2)))
        self.status_label = Label(text="جاري الاستماع...", font_size='20sp', color=(0, 1, 0, 1), size_hint=(1, 0.2))
        self.add_widget(self.status_label)
        threading.Thread(target=self.listen_loop, daemon=True).start()

    def listen_loop(self):
        recognizer = sr.Recognizer()
        while True:
            try:
                with sr.Microphone() as source:
                    audio = recognizer.listen(source, phrase_time_limit=5)
                    text = recognizer.recognize_google(audio, language="ar-SA")
                    Clock.schedule_once(lambda dt, t=text: self.update_status(f"سمعت: {t}"))
            except Exception:
                pass

    def update_status(self, text):
        self.status_label.text = text

class JarvixApp(App):
    def build(self):
        return JarvixMobileUI()

if name == "main":
    JarvixApp().run()
