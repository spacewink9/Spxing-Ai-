import tkinter as tk

class VoiceCommandWidget(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.voice_command_label = tk.Label(self, text="Voice Command:")
        self.voice_command_label.pack(side="left")
        self.voice_command_entry = tk.Entry(self)
        self.voice_command_entry.pack(side="left", padx=10)
        self.voice_command_button = tk.Button(self, text="Submit", command=self.handle_voice_command)
        self.voice_command_button.pack(side="left", padx=10)

    def handle_voice_command(self):
        voice_command = self.voice_command_entry.get()
        # Code to process the voice command using the Spxing AI system
        print("Processing voice command:", voice_command)

class FullScreenWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen', True)
        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.exit_fullscreen)
        self.create_widgets()

    def toggle_fullscreen(self, event=None):
        self.attributes('-fullscreen', not self.attributes('-fullscreen'))

    def exit_fullscreen(self, event=None):
        self.attributes('-fullscreen', False)

    def create_widgets(self):
        self.voice_command_widget = VoiceCommandWidget(self)
        self.voice_command_widget.pack()

if __name__ == "__main__":
    app = FullScreenWindow()
    app.mainloop()
