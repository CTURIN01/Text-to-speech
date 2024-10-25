import pyttsx3
import tkinter as tk
from tkinter import ttk

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Text to Speech")
        self.master.geometry("400x300")

        self.engine = pyttsx3.init()

        self.create_widgets()

    def create_widgets(self):
        # Text input
        self.text_label = ttk.Label(self.master, text="Enter text to speak:")
        self.text_label.pack(pady=10)

        self.text_entry = tk.Text(self.master, height=5, width=40)
        self.text_entry.pack(pady=10)

        # Voice selection
        self.voice_label = ttk.Label(self.master, text="Select Voice:")
        self.voice_label.pack()

        voices = self.engine.getProperty('voices')
        self.voice_var = tk.StringVar()
        self.voice_combobox = ttk.Combobox(self.master, textvariable=self.voice_var)
        self.voice_combobox['values'] = [voice.name for voice in voices]
        self.voice_combobox.set(voices[0].name)
        self.voice_combobox.pack(pady=5)

        # Rate adjustment
        self.rate_label = ttk.Label(self.master, text="Rate:")
        self.rate_label.pack()

        self.rate_var = tk.DoubleVar(value=200)
        self.rate_scale = ttk.Scale(self.master, from_=100, to=300, variable=self.rate_var, orient='horizontal')
        self.rate_scale.pack()

        # Speak button
        self.speak_button = ttk.Button(self.master, text="Speak", command=self.speak)
        self.speak_button.pack(pady=20)

    def speak(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        if text:
            self.engine.setProperty('rate', self.rate_var.get())
            voices = self.engine.getProperty('voices')
            selected_voice = [voice for voice in voices if voice.name == self.voice_var.get()][0]
            self.engine.setProperty('voice', selected_voice.id)
            self.engine.say(text)
            self.engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()